from .Users import Users
from src.users.repositories.core import UsersRepository, UserToCreate, UserToUpdate


__all__ = ['UsersService']


class UsersService:
    def __init__(self, repository: UsersRepository) -> None:
        self.repository = repository

    async def get_by_id(self, user_id: int) -> Users:
        return self.repository.get_by_id(user_id)

    async def create(self, dto: UserToCreate) -> None:
        return self.repository.create(Users(**dict(dto)))

    async def update(self, user_id: int, dto: UserToUpdate) -> None:
        return self.repository.update(user_id, Users(id=user_id, **dict(dto)))

    async def delete_by_id(self, user_id: int) -> None:
        return self.repository.delete_by_id(user_id)
