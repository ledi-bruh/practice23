from pydantic import BaseModel


__all__ = ['UserToUpdate']


class UserToUpdate(BaseModel):

    __slots__ = ('firstname', 'middlename', 'lastname', )

    firstname: str
    middlename: str
    lastname: str
