from pydantic import UUID4
from src.users.application.impl import UsersService
from src.users.domain.dto import UserToCreate, UserToUpdate
from src.users.domain.mappers import user_domain_to_ui
from .models import UserUI

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
