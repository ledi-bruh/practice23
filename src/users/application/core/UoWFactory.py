import typing as t

from ..impl.UnitOfWork import UnitOfWork


__all__ = ['UoWFactory']


class UoWFactory:

    __slots__ = ()

    def __call__(self, repository_config: t.Mapping[str, t.Any]) -> UnitOfWork:
        raise NotImplementedError()
