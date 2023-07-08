from pydantic import UUID4
from src.users.application import UsersService
from ..infrastructure.repositories.core import UserToCreate, UserToUpdate


__all__ = ['UsersView']


class UsersView:

    __slots__ = ('__users_service', )

    def __init__(self, users_service: UsersService) -> None:
        self.__users_service = users_service

    async def get_by_guid(self, user_guid: UUID4):
        return await self.__users_service.get_by_guid(user_guid)

    async def add(self, dto: UserToCreate):
        return await self.__users_service.create(dto)

    async def update(self, user_guid: UUID4, dto: UserToUpdate):
        return await self.__users_service.update(user_guid, dto)

    async def delete_by_guid(self, user_guid: UUID4):
        return await self.__users_service.delete_by_guid(user_guid)
