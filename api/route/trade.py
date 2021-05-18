from flask_restful import Resource, reqparse

from binance_f.base.printobject import PrintBasic, PrintMix

from api import get_server


class ChangeMarginType(Resource):
    def get(self):
        server = get_server()

        parser = reqparse.RequestParser()
        parser.add_argument("symbol", type=str)
        parser.add_argument("marginType", type=str)
        args = parser.parse_args()

        result = server.request.change_margin_type(args.symbol, args.marginType)
        PrintBasic.print_obj(result)


class ChangeLeverage(Resource):
    def get(self):
        server = get_server()

        parser = reqparse.RequestParser()
        parser.add_argument("symbol", type=str)
        parser.add_argument("leverage", type=int)
        args = parser.parse_args()

        result = server.request.change_initial_leverage(args.symbol, args.leverage)
        PrintBasic.print_obj(result)


class PostOrder(Resource):
    def get(self):
        server = get_server()

        parser = reqparse.RequestParser()
        parser.add_argument("symbol", type=str)
        parser.add_argument("side", type=str)
        parser.add_argument("ordertype", type=str)
        parser.add_argument("stopPrice", type=int)
        parser.add_argument("closePosition", type=bool)
        parser.add_argument("positionSide", type=str)
        args = parser.parse_args()

        result = server.request.post_order(
            args.symbol,
            args.side,
            args.ordertype,
            args.stopPrice,
            args.closePosition,
            args.positionSide,
        )
        PrintMix.print_data(result)
