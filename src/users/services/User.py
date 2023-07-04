from pydantic import BaseModel, UUID4


__all__ = ['User']


class User(BaseModel):

    guid: UUID4
    firstname: str
    middlename: str
    lastname: str
