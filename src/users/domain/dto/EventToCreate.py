from pydantic import BaseModel

from .EventTypeCreateUpdate import EventTypeCreateUpdate
from .IntervalCreateUpdate import IntervalCreateUpdate


__all__ = ['EventToCreate']


class EventToCreate(BaseModel):
    event_type: EventTypeCreateUpdate
    interval: IntervalCreateUpdate
