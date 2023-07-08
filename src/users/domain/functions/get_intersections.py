import typing as t
from itertools import pairwise

from ..models.Event import Event


__all__ = ['get_intersections']


def get_intersections(events: t.Iterable[Event]) -> t.Collection[t.Tuple[Event, Event]]:
    sorted_events = sorted(events, key=lambda x: x.interval.starts_at)
    return list(
        filter(
            lambda pair: pair[0].interval.ends_at > pair[1].interval.starts_at,
            pairwise(sorted_events)
        )
    )
