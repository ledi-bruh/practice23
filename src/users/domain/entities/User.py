import typing as t
from copy import deepcopy
from uuid import UUID, uuid4
from itertools import chain

from .Event import Event
from ..value_objects import Name, EventType, Interval
from ..functions import get_intersections
from ..dto import EventToCreate, EventToUpdate


__all__ = ['User']


class User:

    def __init__(self, name: Name):
        self._id = uuid4()
        self._name = name
        self._events: t.List[Event] = []
        self._events_map: t.MutableMapping[UUID, Event] = {}

    @property
    def name(self):
        return self._name

    @property
    def events(self):
        return self._events

    def __check_events(events: t.Iterable[Event]) -> None:
        if len(events) == 0:
            raise Exception('Nothing to check.')

        if len((intersections := get_intersections(events))) > 0:
            raise Exception(f'Events intersect: {intersections}.')

    def add_events(self, events_to_create: t.List[EventToCreate]) -> None:
        events = list(map(
            lambda x: Event(
                event_type=EventType(
                    in_shift=x.event_type.in_shift,
                    is_work=x.event_type.is_work,
                ),
                interval=Interval(
                    starts_at=x.interval.starts_at,
                    ends_at=x.interval.ends_at,
                ),
            ),
            events_to_create
        ))
        self.__check_events(chain(self._events, events))
        self._events += events
        self._events_map.update({event.id: event for event in events})

    def delete_event(self, event_id: UUID) -> None:
        event = self._events_map.pop(event_id)
        self._events.remove(event)

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
        new_events.remove(event)
        new_events.append(new_event)
        self.__check_events(new_events)

        self._events.remove(event)
        self._events.append(new_event)
        self._events_map[event.id] = new_event
