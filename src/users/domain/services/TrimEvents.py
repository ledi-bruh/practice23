import typing as t

from ..entities.User import User
from ..entities.Event import Event
from ..value_objects.Interval import Interval


__all__ = ['TrimEvents']


class TrimEvents:

    def trim_for(self, user: User, events: t.List[Event]) -> None:
        user_events = user.events.copy()
        sorted_events = sorted(events, key=lambda x: x.interval.starts_at)
        interval = Interval(sorted_events[0].interval.starts_at, sorted_events[-1].interval.ends_at)
        events_to_delete = []

        for event in user_events:
            if event.interval.starts_at > interval.starts_at and event.interval.ends_at < interval.ends_at:
                events_to_delete.append(event)

            elif interval.starts_at < event.interval.starts_at < interval.ends_at:
                if event.event_type.is_work and not sorted_events[-1].event_type.in_shift:
                    user.update_event(event.id, ...)  #! EventToUpdate(new_starts)
                else:
                    events_to_delete.append(event)

            elif interval.starts_at < event.interval.ends_at < interval.ends_at:
                if event.event_type.is_work and not sorted_events[0].event_type.in_shift:
                    user.update_event(event.id, ...)  #! EventToUpdate(new_ends)
                else:
                    events_to_delete.append(event)
            
            for event in events_to_delete:
                user.delete_event(event.id)
