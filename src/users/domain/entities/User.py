import typing as t
from copy import deepcopy
from uuid import UUID, uuid4
from itertools import chain
from operator import attrgetter

from .Event import Event
from .Shift import Shift
from ..value_objects import Name, EventType, Interval
from ..functions import get_intersections, split_events_into_shifts
from ..dto import EventToCreate, EventToUpdate


__all__ = ['User']


class User:

    def __init__(self, name: Name):
        self._id = uuid4()
        self._name = name
        self._events: t.List[Event] = []
        self._events_map: t.MutableMapping[UUID, Event] = {}
        self._shifts: t.List[Shift] = []

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def events(self) -> t.Sequence[Event]:
        return deepcopy(self._events)

    @property
    def shifts(self):
        return self._shifts

    def __check_events(self, events: t.Iterable[Event]) -> None:
        if len(events) == 0:
            raise Exception('Nothing to check.')

        if len((intersections := get_intersections(events))) > 0:
            raise Exception(f'Events intersect: {intersections}.')

    def __make_shifts(self, events: t.Sequence[Event]) -> t.List[Shift]:
        shifts = []

        for events_to_shift in split_events_into_shifts(events):
            sorted_events = sorted(events_to_shift, key=attrgetter('starts_at'))
            shifts.append(Shift(
                interval=Interval(
                    starts_at=sorted_events[0].starts_at,
                    ends_at=sorted_events[-1].ends_at,
                ),
                events=sorted_events,
            ))

        return shifts

    def add_events(self, events_to_create: t.Iterable[EventToCreate]) -> None:
        events = list(map(
            lambda e: Event(
                event_type=EventType(
                    in_shift=e.event_type.in_shift,
                    is_work=e.event_type.is_work,
                ),
                interval=Interval(
                    starts_at=e.interval.starts_at,
                    ends_at=e.interval.ends_at,
                ),
            ),
            events_to_create
        ))
        self.__check_events(tuple(chain(self._events, events)))
        self._events += events
        self._events_map.update({event.id: event for event in events})
        self._shifts = self.__make_shifts(self._events)

    def delete_event(self, event_id: UUID) -> None:
        event = self._events_map.pop(event_id)
        self._events.remove(event)
        self._shifts = self.__make_shifts(self._events)

    def update_event(self, event_id: UUID, event_to_update: EventToUpdate) -> None:
        event = self._events_map[event_id]

        new_event = deepcopy(event)
        new_event._event_type=EventType(
            in_shift=event_to_update.event_type.in_shift,
            is_work=event_to_update.event_type.is_work,
        )
        new_event._interval = Interval(
            starts_at=event_to_update.interval.starts_at,
            ends_at=event_to_update.interval.ends_at,
        )

        new_events = self._events.copy()
        new_events[new_events.index(event)] = new_event
        self.__check_events(new_events)

        self._events[self._events.index(event)] = new_event
        self._events_map[event.id] = new_event

        self._shifts = self.__make_shifts(self._events)
