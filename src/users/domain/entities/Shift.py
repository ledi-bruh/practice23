import typing as t
import datetime as dt
from uuid import uuid4

from .Event import Event
from ..value_objects import Interval


__all__ = ['Shift']


class Shift:

    def __init__(self, interval: Interval, events: t.Sequence[Event]) -> None:
        self._id = uuid4()
        self._interval = interval
        self._events = events

    @property
    def id(self):
        return self._id

    @property
    def interval(self):
        return self._interval

    @property
    def events(self):
        return self._events

    @property
    def work_time(self) -> dt.timedelta:
        return sum(
            [event.ends_at - event.starts_at for event in self._events if event.event_type.is_work],
            start=dt.timedelta(0)
        )
