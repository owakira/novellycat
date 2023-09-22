import typing

from gunicorn.app.base import Application


class GunicornApplication(Application):
    def __init__(self, app: typing.Any, options: dict[typing.Any, typing.Any] | None = None):
        self._options = options
        self._app = app

        super(GunicornApplication, self).__init__()

    def load_config(self) -> None:
        config = {}

        if self._options:
            config = {
                key: value
                for key, value in self._options.items()
                if key in self.cfg.settings and value is not None
            }

        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self) -> typing.Any:
        return self._app
