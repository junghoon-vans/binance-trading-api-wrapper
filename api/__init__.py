import os
import toml
from typing import Optional, NamedTuple

from flask import Flask, jsonify, Response
from marshmallow import ValidationError

from binance import Client

from api.client import MainnetClient, TestnetClient
from api.enum import Environment


class Server(NamedTuple):
    app: Flask
    request: Client


server: Optional[Server] = None


def get_server(env: str = "") -> Server:
    global server
    if server is None:
        app = Flask(__name__)
        app.config.from_file(filename=load_config(env), load=toml.load)  # type: ignore
        app.register_error_handler(ValidationError, _handle_validation_error)
        client = create_client(env=env)

        server = Server(
            app=app,
            request=client,
        )
    return server


def load_config(env: str):
    return "../configs/" + env + ".toml"


def create_client(env: str) -> Client:
    if env == Environment.testing:
        api_key = os.getenv("BINANCE_TESTNET_API_KEY")
        api_secret = os.getenv("BINANCE_TESTNET_SECRET_KEY")
        return TestnetClient(api_key, api_secret)
    else:
        api_key = os.getenv("BINANCE_MAINNET_API_KEY")
        api_secret = os.getenv("BINANCE_MAINNET_SECRET_KEY")
        return MainnetClient(api_key, api_secret)


def _handle_validation_error(e: ValidationError) -> Response:
    response = jsonify({"invalidFields": e.normalized_messages()})
    response.status_code = 400
    return response
