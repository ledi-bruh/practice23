import typing as t
import datetime as dt
from uuid import uuid4

from ..value_objects.EventType import EventType


__all__ = ['Shift']


class Shift:

    __slots__ = (
        'id',
        'event_type',
        'starts_at',
        'ends_at',
        'work_time',
    )

    def __init__(self, event_type: EventType, starts_at: dt.datetime, ends_at: dt.datetime) -> None:
        self.id = uuid4()
        self.event_type = event_type
        self.starts_at = starts_at
        self.ends_at = ends_at

    def __eq__(self, __value: object) -> bool:
        return self.id == __value.id
