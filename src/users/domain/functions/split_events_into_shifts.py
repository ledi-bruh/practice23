import typing as t
from itertools import pairwise, chain

from ..entities import Event


__all__ = ['split_events_into_shifts']


def split_events_into_shifts(events: t.Sequence[Event]) -> t.List[t.Tuple[Event]]:
    shifts = []
    shift = []

    for event, next_event in pairwise(chain(events, events[-1:])):
        if not event.event_type.in_shift:
            continue

        shift.append(event)

        if not next_event.event_type.in_shift:
            shifts.append(tuple(shift))
            shift.clear()
            continue

        if event.ends_at < next_event.starts_at:
            shifts.append(tuple(shift))
            shift.clear()

    shifts.append(tuple(shift))

    return list(filter(lambda work_shift: len(work_shift) > 0, shifts))
