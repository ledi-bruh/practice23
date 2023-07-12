import typing as t
from uuid import UUID

from src.users.domain import (
    User, UserToCreate, UserToUpdate,
    Event, EventToCreate, EventToUpdate,
    Interval, IntervalCreateUpdate,
    Name,
    UpdateUserEventsByInterval,
)
from src.users.infrastructure import UsersRepository


__all__ = ['UsersService']


class UsersService:

    __slots__ = (
        '__unit_of_work',
        '__users_repository',
        '__update_user_events_by_interval',
    )

    def __init__(
        self,
        unit_of_work: ...,
        users_repository: UsersRepository,
        update_user_events_by_interval: UpdateUserEventsByInterval,
    ) -> None:
        self.__unit_of_work = unit_of_work,
        self.__users_repository = users_repository
        self.__update_user_events_by_interval = update_user_events_by_interval

    async def get_by_id(self, user_id: UUID) -> User:
        return self.__users_repository.get_by_id(user_id)

    async def create(self, user_to_create: UserToCreate) -> None:
        with self.__unit_of_work as uow:
            self.__users_repository.create(User(**dict(user_to_create)))  #! commit here with UoW

            uow.commit()  #! Лучше явно commit или неявно?

    async def update(self, user_id: UUID, user_to_update: UserToUpdate) -> None:
        with self.__unit_of_work as uow:
            user = await self.get_by_id(user_id)
            user._name = Name(**dict(user_to_update.name))  #! Использовать xxx или _xxx?

            self.__users_repository.update(user_id, user)

            uow.commit()

    async def delete_by_id(self, user_id: UUID) -> None:
        with self.__unit_of_work as uow:
            self.__users_repository.delete_by_id(user_id)

            uow.commit()

    async def get_user_events(self, user: User) -> t.List[Event]:
        return user.events

    #! А если нужно получить вообще все ивенты все юзеров, понадобится новый репозиторий?

    async def add_events(self, user: User, events_to_create: t.List[EventToCreate]) -> None:
        with self.__unit_of_work as uow:
            user.add_events(events_to_create)
            self.__users_repository.update(user.id, user)

            uow.commit()

    async def update_event(self, user: User, event_id: UUID, event_to_update: EventToUpdate) -> None:
        with self.__unit_of_work as uow:
            user.update_event(event_id, event_to_update)
            self.__users_repository.update(user.id, user)

            uow.commit()

    async def delete_event(self, user: User, event_id: UUID) -> None:
        with self.__unit_of_work as uow:
            user.delete_event(event_id)
            self.__users_repository.update(user.id, user)

            uow.commit()

    async def update_user_events_by_interval(
        self,
        user_id: UUID,
        interval: IntervalCreateUpdate, #! IntervalCreateUpdate or Interval
        events_to_create: t.List[EventToCreate],
    ) -> None:
        with self.__unit_of_work as uow:
            user = await self.get_by_id(user_id)
            self.__update_user_events_by_interval(user, Interval(**dict(interval)), events_to_create)

            uow.commit()
