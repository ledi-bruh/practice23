import typing as t
from uuid import UUID

from src.users.domain import User
from ....core import UsersRepository, UserNotFoundException


__all__ = [
    'UsersMemoryRepository',
]


class UsersMemoryRepository(UsersRepository):

    __slots__ = ('__session', )

    def __init__(self) -> None:
        self.__session: t.MutableMapping[int, User] = {}

    def get_by_id(self, id: UUID) -> User:
        """Получить пользователя по id"""

        if (user := self.__session.get(id)) is None:
            raise UserNotFoundException()

        return user

    def create(self, user: User) -> None:
        """Создание пользователя"""

        self.__session[user._id] = user

    def update(self, id: UUID, user: User) -> None:
        """Изменить пользователя"""

        user_to_update = self.__session.get(id)

        for field, value in user:
            setattr(user_to_update, field, value)

    def delete_by_id(self, id: UUID) -> None:
        """Удалить пользователя по id"""

        self.__session.pop(id)
