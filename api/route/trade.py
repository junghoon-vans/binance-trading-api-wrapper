from flask import request
from flask_restful import Resource

from api import get_server


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


class PostOrder(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        server.request.futures_create_order(**params)
