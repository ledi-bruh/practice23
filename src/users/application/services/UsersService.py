from uuid import UUID

from src.users.domain import User
from src.users.infrastructure import UsersRepository, UserToCreate, UserToUpdate


__all__ = [
    'UsersService',
]


class UsersService:

    __slots__ = ('__repository', )

    def __init__(self, repository: UsersRepository) -> None:
        self.__repository = repository

    async def get_by_id(self, user_id: UUID) -> User:
        return self.__repository.get_by_id(user_id)

    async def create(self, dto: UserToCreate) -> None:  #! user_to_create
        return self.__repository.create(User(**dict(dto)))

    async def update(self, user_id: UUID, dto: UserToUpdate) -> None:
        return self.__repository.update(user_id, User(id=user_id, **dict(dto)))

    async def delete_by_id(self, user_id: UUID) -> None:
        return self.__repository.delete_by_id(user_id)

# use cases: add_events ...
