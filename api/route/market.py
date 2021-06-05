from flask import request, jsonify, Response

from api import get_server
from api.schema import (
    market_get_order_book_schema,
    market_get_recent_trades_schema,
    market_get_aggregate_trades_schema,
    market_get_klines_schema,
    market_get_continous_klines_schema,
    market_get_historical_klines_schema,
    market_post_historical_klines_schema,
    market_get_mark_price_schema,
    market_get_funding_rate_schema,
    market_get_ticker_price_change_schema,
    market_get_symbol_price_ticker_schema,
    market_get_symbol_orderbook_ticker_schema,
    market_get_open_interest_schema,
    market_get_open_interest_statistics_schema,
)
from api.spec import DocumentedBlueprint


blueprint = DocumentedBlueprint("market", __name__, url_prefix="/market")


@blueprint.route("/exchange", methods=["GET"])
def exchange_information() -> Response:
    server = get_server()
    response = jsonify(server.request.futures_exchange_info())
    return response


@blueprint.route("/depth", methods=["GET"])
def order_book() -> Response:
    server = get_server()
    params = market_get_order_book_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_order_book(**params))
    return response


@blueprint.route("/trades", methods=["GET"])
def recent_trades_list() -> Response:
    server = get_server()
    params = market_get_recent_trades_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_recent_trades(**params))
    return response


@blueprint.route("/trades/aggregate", methods=["GET"])
def aggregate_trades_list() -> Response:
    server = get_server()
    params = market_get_aggregate_trades_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_aggregate_trades(**params))
    return response


@blueprint.route("/klines", methods=["GET"])
def klines_or_candle_data() -> Response:
    server = get_server()
    params = market_get_klines_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_klines(**params))
    return response


@blueprint.route("/klines/continous", methods=["GET"])
def continous_klines_or_candle_data() -> Response:
    server = get_server()
    params = market_get_continous_klines_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_continous_klines(**params))
    return response


@blueprint.route("/klines/historical", methods=["GET", "POST"])
def historical_klines() -> Response:
    server = get_server()
    if request.method == "GET":
        params = market_get_historical_klines_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_historical_klines(**params))
    elif request.method == "POST":
        payload = market_post_historical_klines_schema.load(request.get_json())
        response = jsonify(
            server.request.futures_historical_klines_generator(**payload)
        )
    return response


@blueprint.route("/mark-price", methods=["GET"])
def mark_price() -> Response:
    server = get_server()
    params = market_get_mark_price_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_mark_price(**params))
    return response


@blueprint.route("/funding-rate", methods=["GET"])
def get_funding_rate_history() -> Response:
    server = get_server()
    params = market_get_funding_rate_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_funding_rate(**params))
    return response


@blueprint.route("/ticker/24h", methods=["GET"])
def ticker_price_change_statistics() -> Response:
    server = get_server()
    params = market_get_ticker_price_change_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_ticker(**params))
    return response


@blueprint.route("/ticker/price", methods=["GET"])
def symbol_price_ticker() -> Response:
    server = get_server()
    params = market_get_symbol_price_ticker_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_symbol_ticker(**params))
    return response


@blueprint.route("/ticker/depth", methods=["GET"])
def symbol_orderbook_ticker() -> Response:
    server = get_server()
    params = market_get_symbol_orderbook_ticker_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_orderbook_ticker(**params))
    return response


@blueprint.route("/open-interest", methods=["GET"])
def open_interest() -> Response:
    server = get_server()
    params = market_get_open_interest_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_open_interest(**params))
    return response


@blueprint.route("/open-interest/statistics", methods=["GET"])
def open_interest_statistics() -> Response:
    server = get_server()
    params = market_get_open_interest_statistics_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_open_interest_hist(**params))
    return response
