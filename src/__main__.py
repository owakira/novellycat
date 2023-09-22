from sanic import Sanic

from src.config import gather_config
from src.gunicorn_app import GunicornApplication


def run_application() -> None:
    # TODO: Configure logging
    config = gather_config()

    # TODO: Use application builder
    app = Sanic('novellycat')

    options = {
        "bind": f"{config.server.address}:{config.server.port}",
        "worker_class": "uvicorn.workers.UvicornWorker",
        "reload": True,
        "disable_existing_loggers": False,
        "preload_app": True,
    }
    gunicorn_app = GunicornApplication(app, options)
    gunicorn_app.run()


if __name__ == '__main__':
    run_application()
