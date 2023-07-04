import typing as t
from uuid import UUID
from src.users.services import User
from src.users.repositories.core import UsersRepository, UserNotFoundException


__all__ = ['UsersMemoryRepository']


class UsersMemoryRepository(UsersRepository):

    __slots__ = ('__session', )

    def __init__(self) -> None:
        self.__session: t.MutableMapping[int, User] = {}

    def get_by_guid(self, guid: UUID) -> User:
        """Получить пользователя по guid"""

        if (user := self.__session.get(guid)) is None:
            raise UserNotFoundException()

        return user

    def create(self, user: User) -> None:
        """Создание пользователя"""

        self.__session[user.guid] = user

    def update(self, guid: UUID, user: User) -> None:
        """Изменить пользователя"""

        user_to_update = self.__session.get(guid)

        for field, value in user:
            setattr(user_to_update, field, value)

    def delete_by_guid(self, guid: UUID) -> None:
        """Удалить пользователя по guid"""

        self.__session.pop(guid)
