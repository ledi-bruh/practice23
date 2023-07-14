from pydantic import BaseModel, UUID4

from .EventUI import EventUI


__all__ = ['UserUI']


class UserUI(BaseModel):
    id: UUID4
    firstname: str
    middlename: str
    lastname: str
    events: list[EventUI]
