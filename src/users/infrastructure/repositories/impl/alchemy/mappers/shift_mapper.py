from uuid import UUID

from src.users.domain import Shift, Interval
from .event_mapper import event_db_to_domain
from ..models import ShiftsAlchemy


__all__ = [
    'shift_domain_to_db',
    'shift_db_to_domain',
]


def shift_domain_to_db(shift: Shift, user_id: UUID) -> ShiftsAlchemy:
    return ShiftsAlchemy(
        id=shift.id,
        user_id=user_id,
        starts_at=shift.interval.starts_at,
        ends_at=shift.interval.ends_at,
        work_time=shift.work_time,
    )


def shift_db_to_domain(db_shift: ShiftsAlchemy) -> Shift:
    shift = Shift.__new__(Shift)
    shift.__dict__.update({'_' + k: v for k, v in db_shift.__dict__.items()})
    shift._interval = Interval(
        starts_at=db_shift.starts_at,
        ends_at=db_shift.ends_at,
    )
    shift._events = list(map(event_db_to_domain, db_shift.events))
    return shift
