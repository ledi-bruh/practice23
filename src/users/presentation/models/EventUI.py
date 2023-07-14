import datetime as dt
from pydantic import BaseModel, UUID4

from .EventTypeUI import EventTypeUI


__all__ = ['EventUI']


class EventUI(BaseModel):
    id: UUID4
    type: EventTypeUI
    starts_at: dt.datetime
    ends_at: dt.datetime
