import typing as t

from ..core.UoWFactory import UoWFactory
from .UnitOfWork import UnitOfWork


__all__ = ['UoWFactoryStore']


class UoWFactoryStore:

    __slots__ = (
        '__factories',
    )

    def __init__(self) -> None:
        self.__factories: t.MutableMapping[str, UoWFactory] = {}

    def register(self, type: str, factory: UoWFactory) -> None:
        self.__factories[type] = factory

    def get_instance(self, type: str, repository_config: t.Mapping[str, t.Any]) -> UnitOfWork:
        if not (factory := self.__factories.get(type)):
            raise Exception(f'{type} factory not found.')

        return factory(repository_config)
