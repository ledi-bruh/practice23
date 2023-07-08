from uuid import uuid4

from ..value_objects import EventType, Interval


__all__ = ['Event']


class Event:

    def __init__(self, event_type: EventType, interval: Interval) -> None:
        self._id = uuid4()
        self._event_type = event_type
        self._interval = interval

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self.id = value

    @property
    def interval(self):
        return self._interval

    @property
    def event_type(self):
        return self._event_type

    @property
    def starts_at(self):
        return self._interval.starts_at

    @property
    def ends_at(self):
        return self._interval.ends_at
