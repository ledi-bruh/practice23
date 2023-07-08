import typing as t
from itertools import pairwise

from src.common.domain import IntervalProtocol


__all__ = [
    'get_intersections',
]


def get_intersections(events: t.Iterable[IntervalProtocol]) -> t.Collection[t.Tuple[IntervalProtocol, IntervalProtocol]]:
    sorted_events: t.List[IntervalProtocol] = sorted(events, key=lambda x: x.starts_at)
    return list(
        filter(
            lambda pair: pair[0].ends_at > pair[1].starts_at,
            pairwise(sorted_events)
        )
    )
