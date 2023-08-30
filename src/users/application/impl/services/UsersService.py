import typing as t
from uuid import UUID

from src.users.domain import User, Event, Interval, Name, UpdateUserEventsByInterval
from src.users.domain.dto import UserToCreate, UserToUpdate, EventToCreate, EventToUpdate, IntervalCreateUpdate
from ...core import UnitOfWork


__all__ = ['UsersService']


class UsersService:

    __slots__ = (
        '__unit_of_work',
        '__update_user_events_by_interval',
    )

    def __init__(
        self,
        unit_of_work: UnitOfWork,
        update_user_events_by_interval: UpdateUserEventsByInterval,
    ) -> None:
        self.__unit_of_work = unit_of_work
        self.__update_user_events_by_interval = update_user_events_by_interval

    async def get_by_id(self, user_id: UUID) -> User:
        return await self.__unit_of_work.users_repository.get_by_id(user_id)

    async def create(self, user_to_create: UserToCreate) -> None:
        with self.__unit_of_work as uow:
            await uow.users_repository.create(User(
                name=Name(**dict(user_to_create.name))
            ))

            await uow.commit()

    async def update(self, user_id: UUID, user_to_update: UserToUpdate) -> None:
        with self.__unit_of_work as uow:
            user = await self.get_by_id(user_id)
            user._name = Name(**dict(user_to_update.name))

            await uow.users_repository.update(user_id, user)

            await uow.commit()

    async def delete_by_id(self, user_id: UUID) -> None:
        with self.__unit_of_work as uow:
            await uow.users_repository.delete_by_id(user_id)

            await uow.commit()

    async def get_user_events(self, user_id: UUID) -> t.Sequence[Event]:
        user = await self.get_by_id(user_id)
        return user.events

    async def add_events(self, user_id: UUID, events_to_create: t.Iterable[EventToCreate]) -> None:
        with self.__unit_of_work as uow:
            user = await self.get_by_id(user_id)
            user.add_events(events_to_create)
            await uow.users_repository.update(user.id, user)

            await uow.commit()

    async def update_event(self, user_id: UUID, event_id: UUID, event_to_update: EventToUpdate) -> None:
        with self.__unit_of_work as uow:
            user = await self.get_by_id(user_id)
            user.update_event(event_id, event_to_update)
            await uow.users_repository.update(user.id, user)

            await uow.commit()

    async def delete_event(self, user_id: UUID, event_id: UUID) -> None:
        with self.__unit_of_work as uow:
            user = await self.get_by_id(user_id)
            user.delete_event(event_id)
            await uow.users_repository.update(user.id, user)

            await uow.commit()

    async def update_user_events_by_interval(
        self,
        user_id: UUID,
        interval: IntervalCreateUpdate,
        events_to_create: t.List[EventToCreate],
    ) -> None:
        with self.__unit_of_work as uow:
            user = await self.get_by_id(user_id)
            await self.__update_user_events_by_interval(user, Interval(**dict(interval)), events_to_create)
            await uow.users_repository.update(user.id, user)

            await uow.commit()
