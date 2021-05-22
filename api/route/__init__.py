from flask import Flask

from .trade import register_trade_route


def init_route(app: Flask):
    register_trade_route(app)
