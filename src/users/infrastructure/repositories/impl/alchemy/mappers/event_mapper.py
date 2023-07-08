from src.users.domain import Event, User, EventType, Interval
from ..models import EventsAlchemy


__all__ = [
    'user_domain_to_db',
    'user_db_to_domain',
]


def event_domain_to_db(event: Event, user: User) -> EventsAlchemy:
    return EventsAlchemy(
        id=event._id,
        user_id=user._id,  #?
        in_shift=event._event_type._in_shift,
        is_work=event._event_type._is_work,
        starts_at=event._interval._starts_at,
        ends_at=event._interval._ends_at,
    )


def event_db_to_domain(db_event: EventsAlchemy) -> Event:
    event = Event.__new__(Event)
    event.__dict__.update({'_' + k: v for k, v in db_event.__dict__.items()})
    event._event_type = EventType(
        in_shift=db_event.in_shift,
        is_work=db_event.is_work,
    )
    event._interval = Interval(
        starts_at=db_event.starts_at,
        ends_at=db_event.ends_at,
    )
    return event
