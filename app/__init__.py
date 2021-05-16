from typing import Any, Dict, Optional, NamedTuple, cast

from flask import Flask
from flask_restful import Api

from binance_f import RequestClient

from app.utils.config_proxy import load_config
from app.request_client import MainnetClient, TestnetClient
from app.network import Network


class Server(NamedTuple):
    app: Flask
    api: Api
    request: RequestClient


server: Optional[Server] = None


def get_server(network: str = "") -> Server:
    global server
    if server is None:
        app = Flask(__name__)
        app.config.update(load_config("default"))
        api = Api(app)

        request_client = None
        network_config = cast(Dict[Any, Any], app.config.get("network"))
        if network == Network.mainnet.value:
            request_client = MainnetClient(network_config)
        elif network == Network.testnet.value:
            request_client = TestnetClient(network_config)
        else:
            raise Exception("only mainnet or testnet can be selected.")

        server = Server(
            app=app,
            api=api,
            request=request_client,
        )
    return server
