from sanic import Sanic

from src.config import gather_config
from src.gunicorn_app import GunicornApplication
from src.logging import configure_logging


def run_application() -> None:
    log_config = configure_logging('log.yml')
    config = gather_config()

    # TODO: Use application builder
    app = Sanic('novellycat', log_config=log_config)

    options = {
        'bind': f'{config.server.address}:{config.server.port}',
        'worker_class': 'uvicorn.workers.UvicornWorker',
        'reload': True,
        'disable_existing_loggers': False,
        'preload_app': True,
        'logconfig_dict': log_config,
    }
    gunicorn_app = GunicornApplication(app, options)
    gunicorn_app.run()


if __name__ == '__main__':
    run_application()
