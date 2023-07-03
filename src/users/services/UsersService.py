from uuid import UUID
from .Users import Users
from src.users.repositories.core import UsersRepository, UserToCreate, UserToUpdate


__all__ = ['UsersService']


class UsersService:

    __slots__ = ('__repository', )

    def __init__(self, repository: UsersRepository) -> None:
        self.__repository = repository

    async def get_by_guid(self, user_guid: UUID) -> Users:
        return self.__repository.get_by_guid(user_guid)

    async def create(self, dto: UserToCreate) -> None:
        return self.__repository.create(Users(**dict(dto)))

    async def update(self, user_guid: UUID, dto: UserToUpdate) -> None:
        return self.__repository.update(user_guid, Users(guid=user_guid, **dict(dto)))

    async def delete_by_guid(self, user_guid: UUID) -> None:
        return self.__repository.delete_by_guid(user_guid)
