from pydantic import BaseModel

from .NameCreateUpdate import NameCreateUpdate


__all__ = ['UserToUpdate']


class UserToUpdate(BaseModel):
    name: NameCreateUpdate
