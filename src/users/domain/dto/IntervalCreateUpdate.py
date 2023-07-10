import datetime as dt
from pydantic import BaseModel


__all__ = ['IntervalCreateUpdate']


class IntervalCreateUpdate(BaseModel):
    starts_at: dt.datetime
    ends_at: dt.datetime
