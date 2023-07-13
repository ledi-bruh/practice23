from src.users.infrastructure.repositories.core import Connection, UsersRepository


__all__ = ['UnitOfWork']


class UnitOfWork:

    __slots__ = (
        '__connection',
        'users_repository',
    )

    def __init__(self, connection: Connection, users_repository: UsersRepository) -> None:
        self.__connection = connection
        self.users_repository = users_repository

    def __enter__(self) -> 'UnitOfWork':
        return self

    def __exit__(self, *args) -> None:
        self.rollback()

    def commit(self) -> None:
        self.__connection.commit()

    def rollback(self) -> None:
        self.__connection.rollback()
