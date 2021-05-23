from flask import Blueprint, request

from api import get_server


blueprint = Blueprint("market", __name__, url_prefix="/market")


@blueprint.route("/order_book/")
def order_book():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_order_book(**params)


@blueprint.route("/recent_trades/")
def recent_trades():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_recent_trades(**params)


@blueprint.route("/historical_trades/")
def historical_trades():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_historical_trades(**params)


@blueprint.route("/aggregate_trades/")
def aggregate_trades():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_aggregate_trades(**params)


@blueprint.route("/klines/")
def klines():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_klines(**params)


@blueprint.route("/continous_klines/")
def continous_klines():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_continous_klines(**params)


@blueprint.route("/historical_klines/")
def historical_klines():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_historical_klines(**params)


@blueprint.route("/historical_klines_generator/")
def historical_klines_generator():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_historical_klines_generator(**params)


@blueprint.route("/mark_price/")
def mark_price():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_mark_price(**params)


@blueprint.route("/funding_rate/")
def funding_rate():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_funding_rate(**params)


@blueprint.route("/ticker/")
def ticker():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_ticker(**params)


@blueprint.route("/symbol_ticker/")
def symbol_ticker():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_symbol_ticker(**params)


@blueprint.route("/orderbook_ticker/")
def orderbook_ticker():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_orderbook_ticker(**params)


@blueprint.route("/liquidation_orders/")
def liquidation_orders():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_liquidation_orders(**params)


@blueprint.route("/open_interest/")
def open_interest():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_open_interest(**params)


@blueprint.route("/open_interest_hist/")
def open_interest_hist():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_open_interest_hist(**params)
