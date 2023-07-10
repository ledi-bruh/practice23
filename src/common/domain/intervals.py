import typing as t
import datetime as dt


__all__ = [
    'IntervalProtocol',
]


class IntervalAttributeProtocol(t.Protocol):
    
    starts_at: dt.datetime
    ends_at: dt.datetime


class IntervalPropertyProtocol(t.Protocol):

    @property
    def starts_at(self):
        ...

    @property
    def ends_at(self):
        ...


IntervalProtocol = t.Union[IntervalAttributeProtocol, IntervalPropertyProtocol]
