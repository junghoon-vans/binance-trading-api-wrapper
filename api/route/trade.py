from flask import Flask, Blueprint, request
from flask_restful import Api, Resource

from api import get_server


def register_trade_route(app: Flask):
    trade_blueprint = Blueprint("trade", __name__)
    api = Api(trade_blueprint)

    api.add_resource(ChangeMarginType, "/change_margin_type")
    api.add_resource(ChangeLeverage, "/change_leverage")
    api.add_resource(CreateOrder, "/create_order")

    app.register_blueprint(trade_blueprint, url_prefix="/trade")


class ChangeMarginType(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_change_margin_type(**params)


class ChangeLeverage(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_change_leverage(**params)


class CreateOrder(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        server.request.futures_create_order(**params)
