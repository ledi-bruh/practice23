from uuid import UUID
from src.users.services.User import User


__all__ = ['UsersRepository']


class UsersRepository:

    __slots__ = ()

    def get_by_guid(self, guid: UUID) -> None:
        """Получить пользователя по id"""
        raise NotImplementedError()

    def create(self, user: User) -> User:
        """Создание пользователя"""
        raise NotImplementedError()

    def update(self, guid: UUID, user: User) -> None:
        """Изменить пользователя"""
        raise NotImplementedError()

    def delete_by_guid(self, guid: UUID) -> None:
        """Удалить пользователя по id"""
        raise NotImplementedError()
