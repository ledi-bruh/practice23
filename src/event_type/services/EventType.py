from pydantic import BaseModel


__all__ = ['EventType']


class EventType(BaseModel):

    name: str
    in_shift: bool
    in_work: bool
