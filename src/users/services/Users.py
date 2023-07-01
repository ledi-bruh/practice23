from pydantic import BaseModel


__all__ = ['Users']


class Users(BaseModel):
    id: int
    firstname: str
    middlename: str
    lastname: str
