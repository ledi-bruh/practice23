import typing as t

from ....core import UsersRepositoryBuilder
from .UsersMemoryRepository import UsersMemoryRepository


__all__ = ['UsersMemoryRepositoryBuilder']


class UsersMemoryRepositoryBuilder(UsersRepositoryBuilder):

    __slots__ = ()

    def __call__(self, **kwargs: t.Mapping) -> UsersMemoryRepository:
        return UsersMemoryRepository()
