from flask_restful import Api

from api.route.trade import ChangeMarginType, ChangeLeverage, PostOrder


def binding_route(api: Api):
    api.add_resource(ChangeMarginType, "/trade/change_margin_type")
    api.add_resource(ChangeLeverage, "/trade/change_leverage")
    api.add_resource(PostOrder, "/trade/post_order")
