from pydantic import BaseModel, UUID4


__all__ = [
    'UserToCreate',
]


class UserToCreate(BaseModel):

    firstname: str
    middlename: str
    lastname: str
