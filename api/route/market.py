from flask import Blueprint, request

from api import get_server


blueprint = Blueprint("market", __name__, url_prefix="/market")


@blueprint.route("/depth/")
def order_book():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_order_book(**params)


@blueprint.route("/trades/")
def recent_trades_list():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_recent_trades(**params)


@blueprint.route("/trades/historical/")
def old_trades_lookup():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_historical_trades(**params)


@blueprint.route("/trades/aggregate/")
def aggregate_trades_list():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_aggregate_trades(**params)


@blueprint.route("/klines/")
def klines_or_candle_data():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_klines(**params)


@blueprint.route("/klines/continous/")
def continous_klines_or_candle_data():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_continous_klines(**params)


@blueprint.route("/klines/historical/")
def historical_klines():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_historical_klines(**params)


@blueprint.route("/klines/historical/generator/")
def historical_klines_generator():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_historical_klines_generator(**params)


@blueprint.route("/mark-price/")
def mark_price():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_mark_price(**params)


@blueprint.route("/funding-rate/")
def get_funding_rate_history():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_funding_rate(**params)


@blueprint.route("/ticker/24h/")
def ticker_price_change_statistics():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_ticker(**params)


@blueprint.route("/ticker/price/")
def symbol_price_ticker():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_symbol_ticker(**params)


@blueprint.route("/ticker/depth/")
def symbol_orderbook_ticker():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_orderbook_ticker(**params)


@blueprint.route("/open-interest/")
def open_interest():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_open_interest(**params)


@blueprint.route("/open-interest/statistics/")
def open_interest_statistics():
    params = request.args.to_dict()
    server = get_server()
    return server.request.futures_open_interest_hist(**params)
