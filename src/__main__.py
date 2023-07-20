import uvicorn
from fastapi import FastAPI

from .app import Application, Config, read_config


app = FastAPI(
    title='Summer Practice 2023',
    description='',
    version='0.10',
)

config = Config(**read_config('config.yml'))
application = Application(config=config, app=app)


@app.on_event('startup')
async def startup():
    await application.initialize()


@app.on_event('shutdown')
async def shutdown():
    await application.deinitialize()


if __name__ == '__main__':
    uvicorn.run(
        'src.__main__:app',
        host=config.app['host'],
        port=config.app['port'],
        reload=True,
    )
