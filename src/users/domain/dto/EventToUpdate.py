from pydantic import BaseModel

from .EventTypeCreateUpdate import EventTypeCreateUpdate
from .IntervalCreateUpdate import IntervalCreateUpdate


__all__ = ['EventToUpdate']


class EventToUpdate(BaseModel):
    event_type: EventTypeCreateUpdate
    interval: IntervalCreateUpdate
