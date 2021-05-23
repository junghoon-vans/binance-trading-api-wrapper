from flask import Flask

from .default import blueprint as default_blueprint
from .account import blueprint as account_blueprint
from .market import blueprint as market_blueprint
from .trade import blueprint as trade_blueprint


def init_route(app: Flask):
    app.register_blueprint(default_blueprint)
    app.register_blueprint(account_blueprint)
    app.register_blueprint(market_blueprint)
    app.register_blueprint(trade_blueprint)
