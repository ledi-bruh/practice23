import typing as t

from ...core import UoWFactory, UnitOfWork


__all__ = ['MemoryUoWFactory']


class MemoryUoWFactory(UoWFactory):

    __slots__ = ()

    def __call__(self, repository_config: t.Mapping[str, t.Any]) -> UnitOfWork:
        raise NotImplementedError()
