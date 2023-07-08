from fastapi import FastAPI

from .config import Config
from ..users.application import UsersService
from ..users.presentation import UsersView
from ..users.infrastructure.repositories import (
    UsersRepositoryFactoryStore,
    UsersMemoryRepositoryFactory, UsersAlchemyRepositoryFactory
)


__all__ = ['Application']


class Application:

    __slots__ = ('__config', '__app', )

    def __init__(self, config: Config, app: FastAPI) -> None:
        self.__config = config
        self.__app = app

    async def start(self) -> None:
        users_repository_fabric_store = UsersRepositoryFactoryStore()
        users_repository_fabric_store.register_factory('memory', UsersMemoryRepositoryFactory())
        users_repository_fabric_store.register_factory('alchemy', UsersAlchemyRepositoryFactory())

        users_repository = users_repository_fabric_store.get_instance(
            self.__config.repository.get('type'),
            self.__config.repository,
        )

        users_service = UsersService(users_repository)
        users_view = UsersView(users_service)

        self.__app.add_api_route(
            '/users/{user_guid}',
            endpoint=users_view.get_by_guid,
            methods=['GET'],
            tags=['Получить пользователя'],
        )
        self.__app.add_api_route(
            '/users',
            endpoint=users_view.add,
            methods=['POST'],
            tags=['Создать пользователя'],
        )
        self.__app.add_api_route(
            '/users/{user_guid}',
            endpoint=users_view.update,
            methods=['PUT'],
            tags=['Изменить пользователя'],
        )
        self.__app.add_api_route(
            '/users/{user_guid}',
            endpoint=users_view.delete_by_guid,
            methods=['DELETE'],
            tags=['Удалить пользователя'],
        )

    async def stop(self):
        pass
