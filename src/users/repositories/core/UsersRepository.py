from uuid import UUID
from src.users.services.Users import Users


__all__ = ['UsersRepository']


class UsersRepository:

    def get_by_guid(self, guid: UUID) -> None:
        """Получить пользователя по id"""
        raise NotImplementedError()

    def create(self, user: Users) -> Users:
        """Создание пользователя"""
        raise NotImplementedError()

    def update(self, guid: UUID, user: Users) -> None:
        """Изменить пользователя"""
        raise NotImplementedError()

    def delete_by_guid(self, guid: UUID) -> None:
        """Удалить пользователя по id"""
        raise NotImplementedError()
