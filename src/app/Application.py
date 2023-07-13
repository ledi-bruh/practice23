from fastapi import FastAPI

from .config import Config
from ..users.presentation import UsersView
from ..users.application import UsersService, UoWFactoryStore, AlchemyUoWFactory, MemoryUoWFactory
from ..users.domain import UpdateUserEventsByInterval, TrimUserEventsByInterval


__all__ = ['Application']


class Application:

    __slots__ = (
        '__config',
        '__app',
    )

    def __init__(self, config: Config, app: FastAPI) -> None:
        self.__config = config
        self.__app = app

    async def initialize(self) -> None:
        uow_factory_store = UoWFactoryStore()
        uow_factory_store.register('memory', MemoryUoWFactory())
        uow_factory_store.register('alchemy', AlchemyUoWFactory())

        unit_of_work = uow_factory_store.get_instance(
            self.__config.repository.get('type'),
            self.__config.repository,
        )

        unit_of_work.initialize()

        trim_user_events_by_interval = TrimUserEventsByInterval()
        update_user_events_by_interval = UpdateUserEventsByInterval(trim_user_events_by_interval)

        users_service = UsersService(unit_of_work, update_user_events_by_interval)

        users_view = UsersView(users_service)

        self.__app.add_api_route(
            '/users/{user_guid}',
            endpoint=users_view.get_by_id,
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
            endpoint=users_view.delete_by_id,
            methods=['DELETE'],
            tags=['Удалить пользователя'],
        )

    async def deinitialize(self):
        pass
