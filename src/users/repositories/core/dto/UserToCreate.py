from pydantic import BaseModel


__all__ = ['UserToCreate']


class UserToCreate(BaseModel):
    id: int
    firstname: str
    middlename: str
    lastname: str
