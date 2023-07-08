import typing as t

from .UsersMemoryRepository import UsersMemoryRepository
from ....core import UsersRepositoryFactory


__all__ = [
    'UsersMemoryRepositoryFactory',
]


class UsersMemoryRepositoryFactory(UsersRepositoryFactory):

    __slots__ = ()

    def __call__(self, **kwargs: t.Mapping) -> UsersMemoryRepository:
        return UsersMemoryRepository()
