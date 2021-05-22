from typing import Any, Dict, Optional, NamedTuple, cast

from flask import Flask
from flask.config import Config
from flask_restful import Api

from flasgger import Swagger

from binance import Client

from api.utils.config_proxy import load_config
from api.client import MainnetClient, TestnetClient
from api.environment import Environment


class Server(NamedTuple):
    app: Flask
    api: Api
    swagger: Swagger
    request: Client


server: Optional[Server] = None


def get_server(env: str = "") -> Server:
    global server
    if server is None:
        app = Flask(__name__)
        app.config.update(load_config(env))
        api = Api(app)
        swagger = Swagger(app, parse=True)

        binance_config = get_config(config=app.config, name="binance")
        client = create_client(env=env, config=binance_config)

        server = Server(
            app=app,
            api=api,
            swagger=swagger,
            request=client,
        )
    return server


def get_config(config: Config, name: str):
    return cast(Dict[Any, Any], config.get(name))


def create_client(env: str, config: Dict[Any, Any]) -> Client:
    if env == Environment.testing:
        return TestnetClient(config)
    return MainnetClient(config)
