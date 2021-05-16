from typing import Any, Dict, Optional, NamedTuple, cast

from flask import Flask
from flask.config import Config
from flask_restful import Api

from binance_f import RequestClient

from api.utils.config_proxy import load_config
from api.request_client import MainnetClient, TestnetClient
from api.network import Network


class Server(NamedTuple):
    app: Flask
    api: Api
    request: RequestClient


server: Optional[Server] = None


def get_server(network: str = "", filename: str = "") -> Server:
    global server
    if server is None:
        app = Flask(__name__)
        app.config.update(load_config(filename))
        api = Api(app)

        network_config = get_network_config(app.config)
        request_client = create_request_client(network, network_config)

        server = Server(
            app=app,
            api=api,
            request=request_client,
        )
    return server


def get_network_config(config: Config):
    return cast(Dict[Any, Any], config.get("network"))


def create_request_client(
    network: str, network_config: Dict[Any, Any]
) -> RequestClient:
    if network == Network.mainnet:
        return MainnetClient(network_config)
    elif network == Network.testnet:
        return TestnetClient(network_config)
    else:
        raise Exception("only mainnet or testnet can be selected as network.")
