from pydantic import BaseModel, UUID4


__all__ = ['UserToCreate']


class UserToCreate(BaseModel):
    guid: UUID4
    firstname: str
    middlename: str
    lastname: str
