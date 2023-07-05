import typing as t

from ..core import UsersRepository, UsersRepositoryBuilder


__all__ = ['UsersRepositoryFabric']


class UsersRepositoryFabric:

    __slots__ = ('__builders', )

    def __init__(self) -> None:
        self.__builders: t.MutableMapping[str, UsersRepositoryBuilder] = {}

    def register_builder(self, type: str, builder: UsersRepositoryBuilder) -> None:
        self.__builders[type] = builder

    def get_instance(self, repository_config: t.Mapping) -> UsersRepository:
        type = repository_config.get('type')

        if not (builder := self.__builders.get(type)):
            raise Exception(f'UsersRepositoryBuilder with type {type} not found.')

        return builder(repository_config=repository_config)
