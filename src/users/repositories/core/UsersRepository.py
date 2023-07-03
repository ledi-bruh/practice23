from src.users.services.Users import Users


__all__ = ['UsersRepository']


class UsersRepository:

    def get_by_guid(self, guid: str) -> None:
        """Получить пользователя по id"""
        raise NotImplementedError()

    def create(self, user: Users) -> Users:
        """Создание пользователя"""
        raise NotImplementedError()

    def update(self, guid: str, user: Users) -> None:
        """Изменить пользователя"""
        raise NotImplementedError()

    def delete_by_guid(self, guid: str) -> None:
        """Удалить пользователя по id"""
        raise NotImplementedError()
