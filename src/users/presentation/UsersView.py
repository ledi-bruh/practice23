from src.users.services import UsersService
from src.users.repositories.core import UserToCreate, UserToUpdate


__all__ = ['UsersView']


class UsersView:

    def __init__(self, users_service: UsersService) -> None:
        self.users_service = users_service
    
    async def get_by_id(self, user_id: int):
        return await self.users_service.get_by_id(user_id)
    
    async def add(self, dto: UserToCreate):
        return await self.users_service.create(dto)
    
    async def update(self, user_id: int, dto: UserToUpdate):
        return await self.users_service.update(user_id, dto)
    
    # ! Если в параметрах int, то на самом деле принимается str
    async def delete_by_id(self, user_id):
        return await self.users_service.delete_by_id(user_id)
