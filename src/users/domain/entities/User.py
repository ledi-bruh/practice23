import typing as t
from uuid import UUID, uuid4

from .Event import Event
from ..value_objects import Name
from ..services import TrimEvents
from ..functions import get_intersections


__all__ = ['User']


class User:  #! Root

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
        intersections = get_intersections(events)
        if len(intersections) > 0 or len(events) == 0:
            raise Exception('Events intersect')

    def add_events(self, trim_events: TrimEvents, events: ...) -> None:  #! t.List[EventToCreate]
        self.__check_events(events)
        self._events += events
        self._events_map.update({event.id: event for event in events})

    def delete_event(self, event_id: UUID):
        event = self._events_map.pop(event_id)
        self._events.remove(event)

    def update_event(self, event_id: UUID, event_to_update: ...):
        event = self._events_map[event_id]
        
        new_event = Event(
            event_type=event.event_type,
            interval=event.interval,
        )
        new_event.id = event.id

        for k, v in event_to_update:
            setattr(new_event, k, v)

        new_events = self._events.copy()
        new_events.remove(event)
        new_events.append(new_event)
        self.__check_events(new_events)

        for k, v in event_to_update:
            setattr(event, k, v)
