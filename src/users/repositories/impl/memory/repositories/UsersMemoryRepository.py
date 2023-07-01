import typing as t
from src.users.services import Users
from src.users.repositories.core import UsersRepository, UserNotFoundException


__all__ = ['UsersMemoryRepository']


class UsersMemoryRepository(UsersRepository):

    def __init__(self) -> None:
        self.session: t.MutableMapping[int, Users] = {}

    def get_by_id(self, id: int) -> Users:
        """Получить пользователя по id"""

        if (user := self.session.get(id)) is None:
            raise UserNotFoundException()

        return user

    def create(self, user: Users) -> None:
        """Создание пользователя"""

        self.session[user.id] = user

    def update(self, id: int, user: Users) -> None:
        """Изменить пользователя"""

        user_to_update = self.session.get(id)

        for field, value in user:
            setattr(user_to_update, field, value)

    def delete_by_id(self, id: int) -> None:
        """Удалить пользователя по id"""
        print(type(id))
        print(self.session)
        print(self.session.pop(id, None))
