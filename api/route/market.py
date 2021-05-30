from flask import Blueprint, request, jsonify

from api import get_server


blueprint = Blueprint("market", __name__, url_prefix="/market")


@blueprint.route("/exchange-info")
def exchange_info():
    server = get_server()
    response = jsonify(server.request.futures_exchange_info())
    return response


@blueprint.route("/depth")
def order_book():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_order_book(**params)

    return jsonify(response)


@blueprint.route("/trades")
def recent_trades_list():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_recent_trades(**params)

    return jsonify(response)


@blueprint.route("/trades/historical")
def old_trades_lookup():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_historical_trades(**params)

    return jsonify(response)


@blueprint.route("/trades/aggregate")
def aggregate_trades_list():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_aggregate_trades(**params)

    return jsonify(response)


@blueprint.route("/klines")
def klines_or_candle_data():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_klines(**params)

    return jsonify(response)


@blueprint.route("/klines/continous")
def continous_klines_or_candle_data():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_continous_klines(**params)

    return jsonify(response)


@blueprint.route("/klines/historical")
def historical_klines():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_historical_klines(**params)

    return jsonify(response)


@blueprint.route("/klines/historical/generator")
def historical_klines_generator():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_historical_klines_generator(**params)

    return jsonify(response)


@blueprint.route("/mark-price")
def mark_price():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_mark_price(**params)

    return jsonify(response)


@blueprint.route("/funding-rate")
def get_funding_rate_history():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_funding_rate(**params)

    return jsonify(response)


@blueprint.route("/ticker/24h")
def ticker_price_change_statistics():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_ticker(**params)

    return jsonify(response)


@blueprint.route("/ticker/price")
def symbol_price_ticker():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_symbol_ticker(**params)

    return jsonify(response)


@blueprint.route("/ticker/depth")
def symbol_orderbook_ticker():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_orderbook_ticker(**params)

    return jsonify(response)


@blueprint.route("/open-interest")
def open_interest():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_open_interest(**params)

    return jsonify(response)


@blueprint.route("/open-interest/statistics")
def open_interest_statistics():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_open_interest_hist(**params)

    return jsonify(response)
