from pydantic import BaseModel, UUID4


__all__ = ['UserToCreate']


class UserToCreate(BaseModel):

    __slots__ = ('guid', 'firstname', 'middlename', 'lastname', )

    guid: UUID4
    firstname: str
    middlename: str
    lastname: str
