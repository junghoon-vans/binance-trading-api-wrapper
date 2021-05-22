from flask import request
from flask_restful import Api, Resource

from api import get_server


def register_default_route(api: Api):
    api.add_resource(Ping, "/ping")
    api.add_resource(Time, "/time")
    api.add_resource(ExchangeInfo, "/exchange_info")
    api.add_resource(UserStream, "/user_stream")


class Ping(Resource):
    def get(self):
        server = get_server()
        return server.request.futures_ping()


class Time(Resource):
    def get(self):
        server = get_server()
        return server.request.futures_time()


class ExchangeInfo(Resource):
    def get(self):
        server = get_server()
        return server.request.futures_exchange_info()


class UserStream(Resource):
    def get(self):
        server = get_server()
        return server.request.futures_stream_get_listen_key()

    def put(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_stream_keepalive(**params)

    def delete(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_stream_close(**params)
