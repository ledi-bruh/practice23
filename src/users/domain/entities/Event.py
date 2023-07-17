from uuid import uuid4

from ..value_objects import EventType, Interval


__all__ = ['Event']


class Event:

    def __init__(self, event_type: EventType, interval: Interval) -> None:
        self._id = uuid4()
        self._event_type = event_type
        self._interval = interval

    def __repr__(self):
        return f'{self._id}:  {self._interval._starts_at}––{self._interval._ends_at}'

    @property
    def id(self):
        return self._id

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        self._interval = value

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value

    @property
    def starts_at(self):
        return self._interval.starts_at

    @property
    def ends_at(self):
        return self._interval.ends_at
