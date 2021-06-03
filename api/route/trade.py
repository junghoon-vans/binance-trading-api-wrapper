from flask import Blueprint, request, jsonify, Response

from api import get_server
from api.schema import (
    trade_get_order_schema,
    trade_post_order_schema,
    trade_delete_order_schema,
    trade_post_multiple_order_schema,
    trade_delete_multiple_order_schema,
    trade_get_open_order_schema,
    trade_get_all_order_schema,
    trade_delete_all_order_schema,
    trade_change_leverage_schema,
    trade_change_margin_type_schema,
    trade_get_position_margin_schema,
    trade_post_position_margin_schema,
    trade_get_position_mode_schema,
    trade_post_position_mode_schema,
    trade_get_multi_asset_mode_schema,
    trade_post_multi_asset_mode_schema,
)


blueprint = Blueprint("trade", __name__, url_prefix="/trade")


@blueprint.route("/order", methods=["GET", "POST", "DELETE"])
def order() -> Response:
    server = get_server()
    response = Response()

    if request.method == "GET":
        params = trade_get_order_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_get_order(**params))
    elif request.method == "POST":
        params = trade_post_order_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_create_order(**params))
    elif request.method == "DELETE":
        params = trade_delete_order_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_cancel_order(**params))
    return response


@blueprint.route("/order/multiple", methods=["POST", "DELETE"])
def mutiple_orders() -> Response:
    server = get_server()
    response = Response()

    if request.method == "POST":
        params = trade_post_multiple_order_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_place_batch_order(**params))
    elif request.method == "DELETE":
        params = trade_delete_multiple_order_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_cancel_orders(**params))
    return response


@blueprint.route("/order/open")
def get_open_orders() -> Response:
    server = get_server()
    params = trade_get_open_order_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_get_open_orders(**params))
    return response


@blueprint.route("/order/all", methods=["GET", "DELETE"])
def all_orders() -> Response:
    server = get_server()
    response = Response()

    if request.method == "GET":
        params = trade_get_all_order_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_get_all_orders(**params))
    elif request.method == "DELETE":
        params = trade_delete_all_order_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_cancel_all_open_orders(**params))
    return response


@blueprint.route("/leverage", methods=["POST"])
def change_leverage() -> Response:
    server = get_server()
    params = trade_change_leverage_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_change_leverage(**params))
    return response


@blueprint.route("/margin-type", methods=["POST"])
def change_margin_type() -> Response:
    server = get_server()
    params = trade_change_margin_type_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_change_margin_type(**params))
    return response


@blueprint.route("/position-margin", methods=["GET", "POST"])
def position_margin() -> Response:
    server = get_server()
    response = Response()

    if request.method == "GET":
        params = trade_get_position_margin_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_position_margin_history(**params))
    elif request.method == "POST":
        params = trade_post_position_margin_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_change_position_margin(**params))
    return response


@blueprint.route("/mode/position", methods=["GET", "POST"])
def position_mode() -> Response:
    server = get_server()
    response = Response()

    if request.method == "GET":
        params = trade_get_position_mode_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_get_position_mode(**params))
    elif request.method == "POST":
        params = trade_post_position_mode_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_change_position_mode(**params))
    return response


@blueprint.route("mode/multi-asset", methods=["GET", "POST"])
def change_multi_assets_mode() -> Response:
    server = get_server()
    response = Response()

    if request.method == "GET":
        params = trade_get_multi_asset_mode_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_get_multi_assets_mode())
    elif request.method == "POST":
        params = trade_post_multi_asset_mode_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_change_multi_assets_mode(**params))
    return response
