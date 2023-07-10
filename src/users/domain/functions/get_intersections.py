import typing as t
from itertools import pairwise
from operator import attrgetter

from src.common.domain import IntervalProtocol


__all__ = ['get_intersections']


T = t.TypeVar('T', bound=IntervalProtocol)


def get_intersections(events: t.Iterable[T]) -> t.List[t.Tuple[T, T]]:
    sorted_events = sorted(events, key=attrgetter('starts_at'))
    return list(
        filter(
            lambda pair: pair[0].ends_at > pair[1].starts_at,
            pairwise(sorted_events)
        )
    )
