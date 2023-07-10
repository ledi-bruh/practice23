
__all__ = ['EventType']


class EventType:

    __slots__ = (
        '_in_shift',
        '_is_work',
    )

    def __init__(self, in_shift: bool, is_work: bool) -> None:
        self.__check(in_shift, is_work)
        self._in_shift = in_shift
        self._is_work = is_work

    def __check(self, in_shift: bool, is_work: bool) -> None:
        if not in_shift and is_work:
            raise Exception('If in_shift is False, is_work must be False')

    @property
    def in_shift(self):
        return self._in_shift

    @property
    def is_work(self):
        return self._is_work
