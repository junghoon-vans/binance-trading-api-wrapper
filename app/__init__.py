from flask import Flask

from app.utils.config_proxy import load_config


def get_server() -> Flask:
    server = Flask(__name__)
    server.config.update(load_config("default"))
    return server
