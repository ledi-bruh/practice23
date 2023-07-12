from uuid import UUID

from src.users.domain.entities import User


__all__ = ['UsersRepository']


class UsersRepository:

    __slots__ = ()

    def get_by_id(self, id: UUID) -> User:
        """Получить пользователя по id"""
        raise NotImplementedError()

    def create(self, user: User) -> None:
        """Создание пользователя"""
        raise NotImplementedError()

    def update(self, id: UUID, user: User) -> None:
        """Изменить пользователя"""
        raise NotImplementedError()

    def delete_by_id(self, id: UUID) -> None:
        """Удалить пользователя по id"""
        raise NotImplementedError()
