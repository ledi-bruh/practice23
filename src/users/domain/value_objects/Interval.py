import datetime as dt


__all__ = ['Interval']


class Interval:

    __slots__ = (
        '_starts_at',
        '_ends_at',
    )

    def __init__(self, starts_at: dt.datetime, ends_at: dt.datetime) -> None:
        self.__check(starts_at, ends_at)
        self._starts_at = starts_at
        self._ends_at = ends_at

    def __check(self, starts_at: dt.datetime, ends_at: dt.datetime) -> None:
        if ends_at <= starts_at:
            raise Exception('starts_at must be less than ends_at.')

    @property
    def starts_at(self):
        return self._starts_at

    @property
    def ends_at(self):
        return self._ends_at
