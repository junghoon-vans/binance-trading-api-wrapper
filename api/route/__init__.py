from flask import Flask, Blueprint
from flask_restful import Api

from .account import register_account_route
from .default import register_default_route
from .market import register_market_route
from .trade import register_trade_route


_default_blueprint = Blueprint("default", __name__)
_account_blueprint = Blueprint("account", __name__)
_market_blueprint = Blueprint("market", __name__)
_trade_blueprint = Blueprint("trade", __name__)


def init_route(app: Flask):
    default_api = Api(_default_blueprint)
    account_api = Api(_account_blueprint)
    market_api = Api(_market_blueprint)
    trade_api = Api(_trade_blueprint)

    register_default_route(default_api)
    register_account_route(account_api)
    register_market_route(market_api)
    register_trade_route(trade_api)

    app.register_blueprint(_default_blueprint, url_prefix="/")
    app.register_blueprint(_account_blueprint, url_prefix="/account")
    app.register_blueprint(_market_blueprint, url_prefix="/market")
    app.register_blueprint(_trade_blueprint, url_prefix="/trade")
