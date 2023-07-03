import uvicorn
from src.app import app, config


uvicorn.run(
    'src.app:app.app',
    host=config.app['host'],
    port=config.app['port'],
    reload=True,
)
