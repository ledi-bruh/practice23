import datetime as dt
from pydantic import BaseModel, UUID4

from .EventUI import EventUI


__all__ = ['ShiftUI']


class ShiftUI(BaseModel):
    id: UUID4
    starts_at: dt.datetime
    ends_at: dt.datetime
    work_time: dt.timedelta
    events: list[EventUI]
