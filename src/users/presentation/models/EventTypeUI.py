from pydantic import BaseModel, UUID4


__all__ = ['EventTypeUI']


class EventTypeUI(BaseModel):
    in_shift: bool
    is_work: bool
