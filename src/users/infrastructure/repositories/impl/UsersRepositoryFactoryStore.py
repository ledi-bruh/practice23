import typing as t

from ..core import UsersRepository, UsersRepositoryFactory


__all__ = [
    'UsersRepositoryFactoryStore',
]


class UsersRepositoryFactoryStore:

    __slots__ = (
        '__factories',
    )

    def __init__(self) -> None:
        self.__factories: t.MutableMapping[str, UsersRepositoryFactory] = {}

    def register_factory(self, type: str, factory: UsersRepositoryFactory) -> None:
        self.__factories[type] = factory

    def get_instance(self, type: str, repository_config: t.Mapping) -> UsersRepository:
        if not (factory := self.__factories.get(type)):
            raise Exception(f'UsersRepositoryBuilder with type {type} not found.')

        return factory(repository_config=repository_config)
