import typing as t

from src.users.infrastructure.repositories import AlchemyConnection, UsersAlchemyRepository
from ...core import UoWFactory, UnitOfWork


__all__ = ['AlchemyUoWFactory']


class AlchemyUoWFactory(UoWFactory):

    __slots__ = ()

    def __call__(self, repository_config: t.Mapping[str, t.Any]) -> UnitOfWork:
        connection = AlchemyConnection(repository_config)
        users_repository = UsersAlchemyRepository(connection)
        return UnitOfWork(connection, users_repository)
