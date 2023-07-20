import typing as t
from pydantic import UUID4
from src.users.application.impl import UsersService
from src.users.domain.dto import UserToCreate, UserToUpdate, EventToCreate, EventToUpdate, IntervalCreateUpdate
from src.users.domain.mappers import user_domain_to_ui, event_domain_to_ui
from ..models import UserUI, EventUI

__all__ = ['UsersView']


class UsersView:

    __slots__ = ('__users_service', )

    def __init__(self, users_service: UsersService) -> None:
        self.__users_service = users_service

    async def get_by_id(self, user_id: UUID4) -> UserUI:
        user = await self.__users_service.get_by_id(user_id)
        return user_domain_to_ui(user)

    async def add(self, dto: UserToCreate) -> None:
        return await self.__users_service.create(dto)

    async def update(self, user_guid: UUID4, dto: UserToUpdate) -> None:
        return await self.__users_service.update(user_guid, dto)

    async def delete_by_id(self, user_id: UUID4) -> None:
        return await self.__users_service.delete_by_id(user_id)

    async def get_user_events(self, user_id: UUID4) -> t.List[EventUI]:
        return list(map(event_domain_to_ui, await self.__users_service.get_user_events(user_id)))

    async def add_events(self, user_id: UUID4, events_to_create: t.List[EventToCreate]) -> None:
        return await self.__users_service.add_events(user_id, events_to_create)

    async def update_event(self, user_id: UUID4, event_id: UUID4, event_to_update: EventToUpdate) -> None:
        return await self.__users_service.update_event(user_id, event_id, event_to_update)

    async def delete_event(self, user_id: UUID4, event_id: UUID4) -> None:
        return await self.__users_service.delete_event(user_id, event_id)

    async def update_user_events_by_interval(
        self,
        user_id: UUID4,
        interval: IntervalCreateUpdate,
        events_to_create: t.List[EventToCreate],
    ) -> None:
        return await self.__users_service.update_user_events_by_interval(user_id, interval, events_to_create)
