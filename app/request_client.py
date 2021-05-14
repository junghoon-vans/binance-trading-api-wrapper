from typing import Optional
from flask import Flask
from binance_f import RequestClient


request_client: Optional[Flask] = None


def set_request_client(server: Flask, network: str):
    global request_client

    network_config = server.config.get(network)
    request_client = RequestClient(
        api_key=network_config.get("api_key"),
        secret_key=network_config.get("secret_key"),
        url=network_config.get("url"),
    )


def get_request_client():
    return request_client
