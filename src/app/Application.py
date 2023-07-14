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
        '__unit_of_work',
    )

    def __init__(self, config: Config, app: FastAPI) -> None:
        self.__config = config
        self.__app = app
        self.__bootstrap()

    def __bootstrap(self):
        uow_factory_store = UoWFactoryStore()
        uow_factory_store.register('memory', MemoryUoWFactory())
        uow_factory_store.register('alchemy', AlchemyUoWFactory())

        self.__unit_of_work = uow_factory_store.get_instance(
            self.__config.repository.get('type'),
            self.__config.repository,
        )

        trim_user_events_by_interval = TrimUserEventsByInterval()
        update_user_events_by_interval = UpdateUserEventsByInterval(trim_user_events_by_interval)

        users_service = UsersService(self.__unit_of_work, update_user_events_by_interval)

        users_view = UsersView(users_service)

        self.__app.add_api_route(
            '/users/{user_guid}',
            response_model=users_view.get_by_id.__annotations__['return'],
            endpoint=users_view.get_by_id,
            methods=['GET'],
            tags=['Получить пользователя'],
        )
        self.__app.add_api_route(
            '/users',
            response_model=users_view.add.__annotations__['return'],
            endpoint=users_view.add,
            methods=['POST'],
            tags=['Создать пользователя'],
        )
        self.__app.add_api_route(
            '/users/{user_guid}',
            response_model=users_view.update.__annotations__['return'],
            endpoint=users_view.update,
            methods=['POST'],
            tags=['Изменить пользователя'],
        )
        self.__app.add_api_route(
            '/users/{user_guid}',
            response_model=users_view.delete_by_id.__annotations__['return'],
            endpoint=users_view.delete_by_id,
            methods=['DELETE'],
            tags=['Удалить пользователя'],
        )

    async def initialize(self) -> None:
        self.__unit_of_work.initialize()

    async def deinitialize(self):
        self.__unit_of_work.deinitialize()
