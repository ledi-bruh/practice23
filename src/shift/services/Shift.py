import datetime as dt
from pydantic import BaseModel, UUID4


__all__ = ['Shift']


class Shift(BaseModel):

    id: UUID4
    user_id: UUID4
    starts_at: dt.datetime
    ends_at: dt.datetime
    work_time: dt.timedelta
