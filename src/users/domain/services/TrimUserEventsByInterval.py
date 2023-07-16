from src.common.domain import IntervalProtocol
from ..entities import User
from ..dto import EventToUpdate, EventTypeCreateUpdate, IntervalCreateUpdate


__all__ = ['TrimUserEventsByInterval']


class TrimUserEventsByInterval:

    async def __call__(self, user: User, interval: IntervalProtocol) -> None:
        for event in user.events:
            if event.starts_at > interval.starts_at and event.ends_at < interval.ends_at:
                user.delete_event(event.id)

            elif interval.starts_at < event.starts_at < interval.ends_at:
                if event.event_type.in_shift:
                    user.delete_event(event.id)
                else:
                    user.update_event(event.id, EventToUpdate(
                        event_type=EventTypeCreateUpdate(
                            in_shift=event.event_type.in_shift,
                            is_work=event.event_type.is_work,
                        ),
                        interval=IntervalCreateUpdate(
                            starts_at=interval.ends_at,
                            ends_at=event.ends_at,
                        ),
                    ))

            elif interval.starts_at < event.ends_at < interval.ends_at:
                if event.event_type.in_shift:
                    user.delete_event(event.id)
                else:
                    user.update_event(event.id, EventToUpdate(
                        event_type=EventTypeCreateUpdate(
                            in_shift=event.event_type.in_shift,
                            is_work=event.event_type.is_work,
                        ),
                        interval=IntervalCreateUpdate(
                            starts_at=event.starts_at,
                            ends_at=interval.starts_at,
                        ),
                    ))
