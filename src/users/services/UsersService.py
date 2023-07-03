from .Users import Users
from src.users.repositories.core import UsersRepository, UserToCreate, UserToUpdate


__all__ = ['UsersService']


class UsersService:

    def __init__(self, repository: UsersRepository) -> None:
        self.repository = repository

    async def get_by_guid(self, user_guid: str) -> Users:
        return self.repository.get_by_guid(user_guid)

    async def create(self, dto: UserToCreate) -> None:
        return self.repository.create(Users(**dict(dto)))

    async def update(self, user_guid: str, dto: UserToUpdate) -> None:
        return self.repository.update(user_guid, Users(guid=user_guid, **dict(dto)))

    async def delete_by_guid(self, user_guid: str) -> None:
        return self.repository.delete_by_guid(user_guid)
