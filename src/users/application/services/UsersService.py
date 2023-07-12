import typing as t
from uuid import UUID

from src.users.domain import (
    User,
    UserToCreate,
    UserToUpdate,
    Event,
    EventToCreate,
    EventToUpdate,
    Interval,
    IntervalCreateUpdate,
    UpdateUserEventsByInterval,
    Name,
)
from src.users.infrastructure import UsersRepository


__all__ = ['UsersService']


class UsersService:

    __slots__ = ('__users_repository', )

    def __init__(
        self,
        users_repository: UsersRepository,
        events_repository: ...,
    ) -> None:
        self.__users_repository = users_repository
        self.__events_repository = events_repository

    async def get_by_id(self, user_id: UUID) -> User:
        return self.__users_repository.get_by_id(user_id)

    async def create(self, user_to_create: UserToCreate) -> None:
        return self.__users_repository.create(User(**dict(user_to_create)))  #? commit here?

    async def update(self, user_id: UUID, user_to_update: UserToUpdate) -> None:
        user = await self.get_by_id(user_id)
        user._name = Name(**dict(user_to_update.name))

        return self.__users_repository.update(user_id, user)

    async def delete_by_id(self, user_id: UUID) -> None:
        return self.__users_repository.delete_by_id(user_id)

    async def get_event(self, user: User, event_id: UUID) -> Event:  #? get event for user? # user or user_id ?
        return user._events_map[event_id]

    async def add_events(self, user: User, events_to_create: t.List[EventToCreate]) -> None:
        user.add_events(events_to_create)
        #? user.save() ?
        #? EventsRepository? или внутри UsersRepository использовать EventsRepository?
        #? => в UsersRepository должны быть функции для events crud и т.д.

    async def update_event(self, user: User, event_id: UUID, event_to_update: EventToUpdate) -> None:
        user.update_event(event_id, event_to_update)

    async def delete_event(self, user: User, event_id: UUID) -> None:
        user.delete_event(event_id)
        self.__events_repository.delete_by_id(event_id)

    async def update_user_events_by_interval(
        self,
        update_user_events_by_interval: UpdateUserEventsByInterval,  #? в конструктор не надо
        user: User,
        interval: Interval, #? IntervalCreateUpdate
        events_to_create: t.List[EventToCreate],
    ) -> None:
        update_user_events_by_interval(user, interval, events_to_create)
        #? user.save()
