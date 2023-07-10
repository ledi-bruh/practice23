from pydantic import BaseModel


__all__ = ['NameCreateUpdate']


class NameCreateUpdate(BaseModel):
    firstname: str
    middlename: str
    lastname: str
