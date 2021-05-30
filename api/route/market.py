from flask import Blueprint, request, jsonify, Response

from api import get_server


blueprint = Blueprint("market", __name__, url_prefix="/market")


@blueprint.route("/exchange-info")
def exchange_info() -> Response:
    server = get_server()
    response = jsonify(server.request.futures_exchange_info())
    return response


@blueprint.route("/depth")
def order_book() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_order_book(**params))
    return response


@blueprint.route("/trades")
def recent_trades_list() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_recent_trades(**params))
    return response


@blueprint.route("/trades/historical")
def old_trades_lookup() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_historical_trades(**params))
    return response


@blueprint.route("/trades/aggregate")
def aggregate_trades_list() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_aggregate_trades(**params))
    return response


@blueprint.route("/klines")
def klines_or_candle_data() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_klines(**params))
    return response


@blueprint.route("/klines/continous")
def continous_klines_or_candle_data() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_continous_klines(**params))
    return response


@blueprint.route("/klines/historical")
def historical_klines() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_historical_klines(**params))
    return response


@blueprint.route("/klines/historical/generator")
def historical_klines_generator() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_historical_klines_generator(**params))
    return response


@blueprint.route("/mark-price")
def mark_price() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_mark_price(**params))
    return response


@blueprint.route("/funding-rate")
def get_funding_rate_history() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_funding_rate(**params))
    return response


@blueprint.route("/ticker/24h")
def ticker_price_change_statistics() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_ticker(**params))
    return response


@blueprint.route("/ticker/price")
def symbol_price_ticker() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_symbol_ticker(**params))
    return response


@blueprint.route("/ticker/depth")
def symbol_orderbook_ticker() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_orderbook_ticker(**params))
    return response


@blueprint.route("/open-interest")
def open_interest() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_open_interest(**params))
    return response


@blueprint.route("/open-interest/statistics")
def open_interest_statistics() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_open_interest_hist(**params))
    return response
