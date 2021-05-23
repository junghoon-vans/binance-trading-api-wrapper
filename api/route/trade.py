from flask import Blueprint, request

from api import get_server


blueprint = Blueprint("trade", __name__, url_prefix="/trade")


@blueprint.route("/create_order/")
def create_order():
    server = get_server()
    params = request.args.to_dict()
    server.request.futures_create_order(**params)


@blueprint.route("/place_batch_order/")
def place_batch_order():
    server = get_server()
    params = request.args.to_dict()
    server.request.futures_place_batch_order(**params)


@blueprint.route("/get_order/")
def get_order():
    server = get_server()
    params = request.args.to_dict()
    server.request.futures_get_order(**params)


@blueprint.route("/get_open_orders/")
def get_open_orders():
    server = get_server()
    params = request.args.to_dict()
    server.request.futures_get_open_orders(**params)


@blueprint.route("/get_all_orders/")
def get_all_orders():
    server = get_server()
    params = request.args.to_dict()
    server.request.futures_get_all_orders(**params)


@blueprint.route("/cancel_order/")
def cancel_order():
    server = get_server()
    params = request.args.to_dict()
    server.request.futures_cancel_order(**params)


@blueprint.route("/cancel_all_open_orders/")
def cancel_all_open_orders():
    server = get_server()
    params = request.args.to_dict()
    server.request.futures_cancel_all_open_orders(**params)


@blueprint.route("/cancel_orders/")
def cancel_orders():
    server = get_server()
    params = request.args.to_dict()
    server.request.futures_cancel_orders(**params)


@blueprint.route("/change_leverage/")
def change_leverage():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_change_leverage(**params)


@blueprint.route("/change_margin_type/")
def change_margin_type():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_change_margin_type(**params)


@blueprint.route("/change_position_margin/")
def change_position_margin():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_change_position_margin(**params)


@blueprint.route("/change_position_mode/")
def change_position_mode():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_change_position_mode(**params)


@blueprint.route("/get_position_mode/")
def get_position_mode():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_get_position_mode(**params)


@blueprint.route("/change_multi_assets_mode/")
def change_multi_assets_mode():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_change_multi_assets_mode(**params)


@blueprint.route("/get_multi_assets_mode/")
def get_multi_assets_mode():
    server = get_server()
    return server.request.futures_get_multi_assets_mode()
