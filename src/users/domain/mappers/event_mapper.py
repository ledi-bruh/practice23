from src.users.presentation.models import EventUI, EventTypeUI
from ..entities.Event import Event


__all__ = [
    'event_domain_to_ui',
]


def event_domain_to_ui(event: Event) -> EventUI:
    return EventUI(
        id=event.id,
        type=EventTypeUI(
            in_shift=event.event_type.in_shift,
            is_work=event.event_type.is_work,
        ),
        starts_at=event.starts_at,
        ends_at=event.ends_at,
    )
