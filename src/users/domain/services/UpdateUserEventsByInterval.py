import typing as t
from operator import attrgetter

from src.common.domain import IntervalProtocol
from ..entities import User
from ..dto import EventToCreate
from .TrimUserEventsByInterval import TrimUserEventsByInterval


__all__ = ['UpdateUserEventsByInterval']


class UpdateUserEventsByInterval:

    def __init__(self, trim_user_events_by_interval: TrimUserEventsByInterval) -> None:
        self.trim_user_events_by_interval = trim_user_events_by_interval

    def __check_interval_for_events(
        self,
        interval: IntervalProtocol,
        events_to_create: t.List[EventToCreate],
    ) -> None:
        sorted_events = sorted(events_to_create, key=attrgetter('interval.starts_at'))
        if sorted_events[0].interval.starts_at < interval.starts_at or sorted_events[-1].interval.ends_at > interval.ends_at:
            raise Exception('To update events in an interval, they must be in this interval.')

    def __call__(
        self,
        user: User,
        interval: IntervalProtocol,
        events_to_create: t.List[EventToCreate],
    ) -> None:
        self.__check_interval_for_events(interval, events_to_create)
        self.trim_user_events_by_interval(user, interval)
        user.add_events(events_to_create)
