import datetime as dt
from pydantic import BaseModel, UUID4

from src.event_type.services import EventType


__all__ = ['Event']


class Event(BaseModel):

    id: UUID4
    user_id: UUID4
    shift_id: UUID4
    event_type: EventType
    starts_at: dt.datetime
    ends_at: dt.datetime
