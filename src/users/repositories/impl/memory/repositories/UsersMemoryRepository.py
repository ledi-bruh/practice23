import typing as t
from src.users.services import Users
from src.users.repositories.core import UsersRepository, UserNotFoundException


__all__ = ['UsersMemoryRepository']


class UsersMemoryRepository(UsersRepository):

    def __init__(self) -> None:
        self.session: t.MutableMapping[int, Users] = {}

    def get_by_guid(self, guid: str) -> Users:
        """Получить пользователя по id"""

        if (user := self.session.get(guid)) is None:
            raise UserNotFoundException()

        return user

    def create(self, user: Users) -> None:
        """Создание пользователя"""

        self.session[user.guid] = user

    def update(self, guid: str, user: Users) -> None:
        """Изменить пользователя"""

        user_to_update = self.session.get(guid)

        for field, value in user:
            setattr(user_to_update, field, value)

    def delete_by_guid(self, guid: str) -> None:
        """Удалить пользователя по id"""

        self.session.pop(guid)
