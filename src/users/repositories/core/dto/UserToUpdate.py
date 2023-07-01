from pydantic import BaseModel


__all__ = ['UserToUpdate']


class UserToUpdate(BaseModel):
    firstname: str
    middlename: str
    lastname: str
