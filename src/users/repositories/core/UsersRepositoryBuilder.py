import typing as t

from .UsersRepository import UsersRepository


__all__ = ['UsersRepositoryBuilder']


class UsersRepositoryBuilder:

    __slots__ = ()

    def __call__(self, **kwargs: t.Mapping) -> UsersRepository:
        raise NotImplementedError()
