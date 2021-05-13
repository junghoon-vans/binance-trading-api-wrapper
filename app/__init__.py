from typing import Optional

from flask import Flask
from flask_restful import Api

from app.route import binding_route
from app.utils.config_proxy import load_config
from app.request_client import set_request_client


server: Optional[Flask] = None


def get_server() -> Flask:
    global server
    if server is None:
        server = Flask(__name__)
        server.config.update(load_config("default"))
    set_request_client(server)
    return server


def binding_api(app: Flask):
    api = Api(app)
    binding_route(api)
