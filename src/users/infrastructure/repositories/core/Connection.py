
__all__ = ['Connection']


class Connection:

    __slots__ = ()

    async def initialize(self) -> None:
        raise NotImplementedError

    async def deinitialize(self) -> None:
        raise NotImplementedError

    async def commit(self) -> None:
        raise NotImplementedError

    def rollback(self) -> None:
        raise NotImplementedError
