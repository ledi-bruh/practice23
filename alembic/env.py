from alembic import context
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from src.app import Config, read_config
from src.common.infrastructure import Base
from src.users.infrastructure import UsersAlchemy, EventsAlchemy


config = Config(**read_config('config.yml'))

target_metadata = Base.metadata

connection_string = URL.create(
    drivername=config.repository['db_driver'],
    username=config.repository['db_login'],
    password=config.repository['db_password'],
    host=config.repository['db_host'],
    port=config.repository['db_port'],
    database=config.repository['db_database'],
)
engine = create_engine(connection_string)


def run_migrations_offline() -> None:
    context.configure(
        url=connection_string,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
