from flask import request
from flask_restful import Api, Resource

from api import get_server


def register_trade_route(api: Api):
    api.add_resource(CreateOrder, "/create_order")
    api.add_resource(PlaceBatchOrder, "/place_batch_order")
    api.add_resource(GetOrder, "/get_order")
    api.add_resource(GetOpenOrders, "/get_open_orders")
    api.add_resource(GetAllOrders, "/get_all_orders")
    api.add_resource(CancelOrder, "/cancel_order")
    api.add_resource(CancelAllOpenOrders, "/cancel_all_open_orders")
    api.add_resource(CancelOrders, "/cancel_orders")
    api.add_resource(ChangeLeverage, "/change_leverage")
    api.add_resource(ChangeMarginType, "/change_margin_type")
    api.add_resource(ChangePositionMargin, "/change_position_margin")
    api.add_resource(ChangePositionMode, "/change_position_mode")
    api.add_resource(GetPositionMode, "/get_position_mode")
    api.add_resource(ChangeMultiAssetsMode, "/change_multi_assets_mode")
    api.add_resource(GetMultiAssetsMode, "/get_multi_assets_mode")


class CreateOrder(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        server.request.futures_create_order(**params)


class PlaceBatchOrder(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        server.request.futures_place_batch_order(**params)


class GetOrder(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        server.request.futures_get_order(**params)


class GetOpenOrders(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        server.request.futures_get_open_orders(**params)


class GetAllOrders(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        server.request.futures_get_all_orders(**params)


class CancelOrder(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        server.request.futures_cancel_order(**params)


class CancelAllOpenOrders(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        server.request.futures_cancel_all_open_orders(**params)


class CancelOrders(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        server.request.futures_cancel_orders(**params)


class ChangeLeverage(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_change_leverage(**params)


class ChangeMarginType(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_change_margin_type(**params)


class ChangePositionMargin(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_change_position_margin(**params)


class ChangePositionMode(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_change_position_mode(**params)


class GetPositionMode(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_get_position_mode(**params)


class ChangeMultiAssetsMode(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_change_multi_assets_mode(**params)


class GetMultiAssetsMode(Resource):
    def get(self):
        server = get_server()
        return server.request.futures_get_multi_assets_mode()
