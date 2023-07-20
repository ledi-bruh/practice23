from src.users.presentation.models import ShiftUI
from .event_mapper import event_domain_to_ui
from ..entities.Shift import Shift


__all__ = [
    'shift_domain_to_ui',
]


def shift_domain_to_ui(shift: Shift) -> ShiftUI:
    return ShiftUI(
        id=shift.id,
        starts_at=shift.interval.starts_at,
        ends_at=shift.interval.ends_at,
        work_time=shift.work_time,
        events=list(map(event_domain_to_ui, shift.events)),
    )
