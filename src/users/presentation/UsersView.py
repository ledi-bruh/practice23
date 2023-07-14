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

    async def add(self, dto: UserToCreate) -> int:
        await self.__users_service.create(dto)
        return 201  #! StatusCode(201) class or in endpoint status_code=201 ?

    async def update(self, user_guid: UUID4, dto: UserToUpdate) -> int:
        await self.__users_service.update(user_guid, dto)
        return 200

    async def delete_by_id(self, user_id: UUID4) -> int:
        await self.__users_service.delete_by_id(user_id)
        return 204
