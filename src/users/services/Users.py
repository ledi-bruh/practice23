from pydantic import BaseModel, UUID4


__all__ = ['Users']


class Users(BaseModel):

    guid: UUID4
    firstname: str
    middlename: str
    lastname: str
