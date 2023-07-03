from pydantic import UUID4
from src.users.services import UsersService
from src.users.repositories.core import UserToCreate, UserToUpdate


__all__ = ['UsersView']


class UsersView:

    def __init__(self, users_service: UsersService) -> None:
        self.users_service = users_service

    async def get_by_guid(self, user_guid: UUID4):
        return await self.users_service.get_by_guid(user_guid)

    async def add(self, dto: UserToCreate):
        return await self.users_service.create(dto)

    async def update(self, user_guid: UUID4, dto: UserToUpdate):
        return await self.users_service.update(user_guid, dto)

    async def delete_by_guid(self, user_guid: UUID4):
        return await self.users_service.delete_by_guid(user_guid)
