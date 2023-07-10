from pydantic import BaseModel


__all__ = ['EventTypeCreateUpdate']


class EventTypeCreateUpdate(BaseModel):
    in_shift: bool
    is_work: bool
