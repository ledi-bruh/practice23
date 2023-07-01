from src.users.services.Users import Users


__all__ = ['UsersRepository']


class UsersRepository:

    def get_by_id(self, id: int) -> None:
        """Получить пользователя по id"""
        raise NotImplementedError()

    def create(self, user: Users) -> Users:
        """Создание пользователя"""
        raise NotImplementedError()

    def update(self, id: int, user: Users) -> None:
        """Изменить пользователя"""
        raise NotImplementedError()

    def delete_by_id(self, id: int) -> None:
        """Удалить пользователя по id"""
        raise NotImplementedError()
