from flask_restful import Resource


class Buy(Resource):
    def get(self):
        return {"trade": "buy"}


class Sell(Resource):
    def get(self):
        return {"trade": "sell"}
