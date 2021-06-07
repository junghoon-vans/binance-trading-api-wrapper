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
def exchange_info() -> Response:
    """Exchange Information
    ---
    get:
      description: Current exchange trading rules and symbol information
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    response = jsonify(server.request.futures_exchange_info())
    return response


@blueprint.route("/depth", methods=["GET"])
def order_book() -> Response:
    """Order Book
    ---
    get:
      parameters:
        - in: query
          schema: GetOrderBookSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = market_get_order_book_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_order_book(**params))
    return response


@blueprint.route("/trades", methods=["GET"])
def recent_trade_list() -> Response:
    """Recent Trades List
    ---
    get:
      description: Get recent trades
      parameters:
        - in: query
          schema: GetRecentTradesSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = market_get_recent_trades_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_recent_trades(**params))
    return response


@blueprint.route("/trades/aggregate", methods=["GET"])
def aggregate_trades_list() -> Response:
    """Compressed/Aggregate Trades List
    ---
    get:
      description:
        Get compressed, aggregate trades. Trades that fill at the time,
        from the same order, with the same price will have the quantity aggregated.
      parameters:
        - in: query
          schema: GetAggregateTradesSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = market_get_aggregate_trades_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_aggregate_trades(**params))
    return response


@blueprint.route("/klines", methods=["GET"])
def klines() -> Response:
    """Kline/Candlestick Data
    ---
    get:
      description:
        Kline/candlestick bars for a symbol.
        Klines are uniquely identified by their open time.
      parameters:
        - in: query
          schema: GetKlinesSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = market_get_klines_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_klines(**params))
    return response


@blueprint.route("/klines/continous", methods=["GET"])
def continous_klines() -> Response:
    """Continuous Contract Kline/Candlestick Data
    ---
    get:
      description:
        Kline/candlestick bars for a specific contract type.
        Klines are uniquely identified by their open time.
      parameters:
        - in: query
          schema: GetContinousKlinesSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = market_get_continous_klines_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_continous_klines(**params))
    return response


@blueprint.route("/klines/historical", methods=["GET", "POST"])
def historical_klines() -> Response:
    """Historical Klines
    ---
    get:
      parameters:
        - in: query
          schema: GetHistoricalKlinesSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    post:
      requestBody:
        required: true
        content:
          application/json:
            schema: PostHistoricalKlinesSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
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
    """Mark Price
    ---
    get:
      description: Mark Price and Funding Rate
      parameters:
        - in: query
          schema: GetMarkPriceSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = market_get_mark_price_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_mark_price(**params))
    return response


@blueprint.route("/funding-rate", methods=["GET"])
def funding_rate_history() -> Response:
    """Get Funding Rate History
    ---
    get:
      parameters:
        - in: query
          schema: GetFundingRateSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = market_get_funding_rate_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_funding_rate(**params))
    return response


@blueprint.route("/ticker/daily", methods=["GET"])
def ticker_daily_price_changes() -> Response:
    """24hr Ticker Price Change Statistics
    ---
    get:
      description: 24 hour rolling window price change statistics.
      parameters:
        - in: query
          schema: GetTickerPriceChangeSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = market_get_ticker_price_change_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_ticker(**params))
    return response


@blueprint.route("/ticker/price", methods=["GET"])
def symbol_price_ticker() -> Response:
    """Symbol Price Ticker
    ---
    get:
      description: Latest price for a symbol or symbols.
      parameters:
        - in: query
          schema: GetSymbolPriceTickerSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = market_get_symbol_price_ticker_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_symbol_ticker(**params))
    return response


@blueprint.route("/ticker/depth", methods=["GET"])
def symbol_orderbook_ticker() -> Response:
    """Symbol Order Book Ticker
    ---
    get:
      description: Best price/qty on the order book for a symbol or symbols.
      parameters:
        - in: query
          schema: GetSymbolOrderbookTickerSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = market_get_symbol_orderbook_ticker_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_orderbook_ticker(**params))
    return response


@blueprint.route("/open-interest", methods=["GET"])
def open_interest() -> Response:
    """Open Interest
    ---
    get:
      description: Get present open interest of a specific symbol.
      parameters:
        - in: query
          schema: GetOpenInterestSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = market_get_open_interest_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_open_interest(**params))
    return response


@blueprint.route("/open-interest/statistics", methods=["GET"])
def open_interest_statistics() -> Response:
    """Open Interest Statistics
    ---
    get:
      parameters:
        - in: query
          schema: GetOpenInterestStatisticsSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = market_get_open_interest_statistics_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_open_interest_hist(**params))
    return response
