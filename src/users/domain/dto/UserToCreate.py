from pydantic import BaseModel

from .NameCreateUpdate import NameCreateUpdate


__all__ = ['UserToCreate']


class UserToCreate(BaseModel):
    name: NameCreateUpdate
