from flask_restful import Api

from app.route.trade import Buy, Sell


def binding_route(api: Api):
    api.add_resource(Buy, "/trade/buy")
    api.add_resource(Sell, "/trade/sell")
