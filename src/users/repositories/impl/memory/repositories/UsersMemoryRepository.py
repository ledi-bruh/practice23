import typing as t
from uuid import UUID
from src.users.services import Users
from src.users.repositories.core import UsersRepository, UserNotFoundException


__all__ = ['UsersMemoryRepository']


class UsersMemoryRepository(UsersRepository):

    def __init__(self) -> None:
        self.__session: t.MutableMapping[int, Users] = {}

    def get_by_guid(self, guid: UUID) -> Users:
        """Получить пользователя по id"""

        if (user := self.__session.get(guid)) is None:
            raise UserNotFoundException()

        return user

    def create(self, user: Users) -> None:
        """Создание пользователя"""

        self.__session[user.guid] = user

    def update(self, guid: UUID, user: Users) -> None:
        """Изменить пользователя"""

        user_to_update = self.__session.get(guid)

        for field, value in user:
            setattr(user_to_update, field, value)

    def delete_by_guid(self, guid: UUID) -> None:
        """Удалить пользователя по id"""

        self.__session.pop(guid)
