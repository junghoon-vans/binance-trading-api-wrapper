from flask import request
from flask_restful import Api, Resource

from api import get_server


def register_market_route(api: Api):
    api.add_resource(OrderBook, "/order_book")
    api.add_resource(RecentTrades, "/recent_trades")
    api.add_resource(historicalTrades, "/historical_trades")
    api.add_resource(AggregateTrades, "/aggregate_trades")
    api.add_resource(Klines, "/klines")
    api.add_resource(ContinousKlines, "/continous_klines")
    api.add_resource(HistoricalKlines, "/historical_klnes")
    api.add_resource(HistoricalKlinesGenerator, "/historical_klines_generator")
    api.add_resource(MarkPrice, "/mark_price")
    api.add_resource(FundingRate, "/funding_rate")
    api.add_resource(Ticker, "/ticker")
    api.add_resource(SymbolTicker, "/symbol_ticker")
    api.add_resource(OrderBookTicker, "/orderbook_ticker")
    api.add_resource(LiquidationOrders, "/liquidation_orders")
    api.add_resource(OpenInterest, "/open_interest")
    api.add_resource(OpenInterestHist, "/open_interest_hist")


class OrderBook(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_order_book(**params)


class RecentTrades(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_recent_trades(**params)


class historicalTrades(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_historical_trades(**params)


class AggregateTrades(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_aggregate_trades(**params)


class Klines(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_klines(**params)


class ContinousKlines(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_continous_klines(**params)


class HistoricalKlines(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_historical_klines(**params)


class HistoricalKlinesGenerator(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_historical_klines_generator(**params)


class MarkPrice(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_mark_price(**params)


class FundingRate(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_funding_rate(**params)


class Ticker(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_ticker(**params)


class SymbolTicker(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_symbol_ticker(**params)


class OrderBookTicker(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_orderbook_ticker(**params)


class LiquidationOrders(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_liquidation_orders(**params)


class OpenInterest(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_open_interest(**params)


class OpenInterestHist(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_open_interest_hist(**params)
