from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from src.app.Config import Config, config
from src.users.services import UsersService
from src.users.presentation import UsersView
from src.users.repositories import UsersRepository, UsersMemoryRepository, UsersAlchemyRepository


__all__ = ['Application', 'app']


class Application:

    def __init__(self, config: Config) -> None:
        self.config = config
        self.app = FastAPI(
            title='Test service',
            description='',
            version='0.1',
        )

    def make_session(self):
        connection_string = URL.create(
            drivername=self.config.repository['db_driver'],
            username=self.config.repository['db_login'],
            password=self.config.repository['db_password'],
            host=self.config.repository['db_host'],
            port=self.config.repository['db_port'],
            database=self.config.repository['db_database']
        )

        engine = create_engine(connection_string)

        Session = sessionmaker(
            engine,
            autocommit=False,
            autoflush=False,
        )
        
        return Session()

    def start(self) -> None:
        users_repository: UsersRepository

        if self.config.repository['type'] == 'memory':
            users_repository = UsersMemoryRepository()
        elif self.config.repository['type'] == 'alchemy':
            session = self.make_session()
            users_repository = UsersAlchemyRepository(session)

        users_service = UsersService(users_repository)
        users_view = UsersView(users_service)

        # ! Add и Update должны быть POST? Тогда явно писать в url /add /update?
        self.app.add_api_route(
            '/users',
            endpoint=users_view.get_by_id,
            methods=['GET'],
            tags=['Получить пользователя'],
        )
        self.app.add_api_route(
            '/users',
            endpoint=users_view.add,
            methods=['POST'],
            tags=['Создать пользователя'],
        )
        self.app.add_api_route(
            '/users',
            endpoint=users_view.update,
            methods=['PUT'],
            tags=['Изменить пользователя'],
        )
        self.app.add_api_route(
            '/users',
            endpoint=users_view.delete_by_id,
            methods=['DELETE'],
            tags=['Удалить пользователя'],
        )


app = Application(config)

app.start()
