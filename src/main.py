import sys
import os
from pathlib import Path

if (dir := str(Path(os.getcwd()).parent)) not in sys.path:
    sys.path.insert(0, dir)

import uvicorn
from src.app import app, config


if __name__ == '__main__':
    uvicorn.run(
        f'{Path(__file__).stem}:app.app',
        host=config.app['host'],
        port=config.app['port'],
        reload=True,
    )
