from typing import Optional
from flask import Flask
from binance_f import RequestClient


request_client: Optional[Flask] = None


def set_request_client(server: Flask):
    global request_client
    request_client = RequestClient(
        api_key=server.config.get("g_api_key"),
        secret_key=server.config.get("g_secret_key"),
    )


def get_request_client():
    return request_client
