
__all__ = ['Connection']


class Connection:

    __slots__ = ()

    def initialize(self) -> None:
        raise NotImplementedError

    def deinitialize(self) -> None:
        raise NotImplementedError

    def commit(self) -> None:
        raise NotImplementedError

    def rollback(self) -> None:
        raise NotImplementedError
