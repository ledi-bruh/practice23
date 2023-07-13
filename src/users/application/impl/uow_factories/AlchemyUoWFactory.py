import typing as t

from src.users.infrastructure.repositories import AlchemyConnection, UsersAlchemyRepository
from ...core.UoWFactory import UoWFactory
from ..UnitOfWork import UnitOfWork


__all__ = ['AlchemyUoWFactory']


class AlchemyUoWFactory(UoWFactory):

    __slots__ = ()

    def __call__(self, repository_config: t.Mapping[str, t.Any]) -> UnitOfWork:
        connection = AlchemyConnection(repository_config)
        users_repository = UsersAlchemyRepository(connection._session)
        return UnitOfWork(connection, users_repository)
