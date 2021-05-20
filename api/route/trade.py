from flask_restful import Resource, reqparse
from flasgger import swag_from

from api import get_server


class ChangeMarginType(Resource):
    @swag_from("../docs/change_margin_type.yml")
    def get(self):
        server = get_server()

        parser = reqparse.RequestParser()
        parser.add_argument("symbol", type=str, default="BTCUSDT")
        parser.add_argument("marginType", type=str)
        args = parser.parse_args()

        server.request.change_margin_type(
            symbol=args.symbol, marginType=args.marginType
        )


class ChangeLeverage(Resource):
    @swag_from("../docs/change_leverage.yml")
    def get(self):
        server = get_server()

        parser = reqparse.RequestParser()
        parser.add_argument("symbol", type=str, default="BTCUSDT")
        parser.add_argument("leverage", type=int)
        args = parser.parse_args()

        server.request.change_initial_leverage(
            symbol=args.symbol, leverage=args.leverage
        )


class PostOrder(Resource):
    @swag_from("../docs/post_order.yml")
    def get(self):
        server = get_server()

        parser = reqparse.RequestParser()
        parser.add_argument("symbol", type=str, default="BTCUSDT")
        parser.add_argument("side", type=str)
        parser.add_argument("ordertype", type=str)
        parser.add_argument("timeInForce", type=str, default=None)
        parser.add_argument("quantity", type=float, default=None)
        parser.add_argument("reduceOnly", type=bool, default=None)
        parser.add_argument("price", type=float, default=None)
        parser.add_argument("newClientOrderId", type=str, default=None)
        parser.add_argument("stopPrice", type=float, default=None)
        parser.add_argument("workingType", type=str, default=None)
        parser.add_argument("closePosition", type=bool, default=None)
        parser.add_argument("positionSide", type=str, default=None)
        parser.add_argument("callbackRate", type=float, default=None)
        parser.add_argument("activationPrice", type=float, default=None)
        parser.add_argument("newOrderRespType", type=str, default=None)
        args = parser.parse_args()

        server.request.post_order(
            symbol=args.symbol,
            side=args.side,
            ordertype=args.ordertype,
            timeInForce=args.timeInForce,
            quantity=args.quantity,
            reduceOnly=args.reduceOnly,
            price=args.price,
            newClientOrderId=args.newClientOrderId,
            stopPrice=args.stopPrice,
            workingType=args.workingType,
            closePosition=args.closePosition,
            positionSide=args.positionSide,
            callbackRate=args.callbackRate,
            activationPrice=args.activationPrice,
            newOrderRespType=args.newOrderRespType,
        )
