from flask import request, jsonify, Response

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
    trade_put_leverage_schema,
    trade_put_margin_type_schema,
    trade_get_position_margin_schema,
    trade_put_position_margin_schema,
    trade_put_position_mode_schema,
    trade_put_multi_asset_mode_schema,
)
from api.spec import DocumentedBlueprint


blueprint = DocumentedBlueprint("trade", __name__, url_prefix="/trade")


@blueprint.route("/order", methods=["GET", "POST", "DELETE"])
def order() -> Response:
    server = get_server()
    response = Response()

    if request.method == "GET":
        params = trade_get_order_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_get_order(**params))
    elif request.method == "POST":
        payload = trade_post_order_schema.load(request.get_json())
        response = jsonify(server.request.futures_create_order(**payload))
    elif request.method == "DELETE":
        params = trade_delete_order_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_cancel_order(**params))
    return response


@blueprint.route("/order/multiple", methods=["POST", "DELETE"])
def mutiple_orders() -> Response:
    server = get_server()
    response = Response()

    if request.method == "POST":
        payload = trade_post_multiple_order_schema.load(request.get_json())
        response = jsonify(server.request.futures_place_batch_order(**payload))
    elif request.method == "DELETE":
        params = trade_delete_multiple_order_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_cancel_orders(**params))
    return response


@blueprint.route("/order/open", methods=["GET"])
def open_orders() -> Response:
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


@blueprint.route("/leverage", methods=["PUT"])
def leverage() -> Response:
    server = get_server()
    payload = trade_put_leverage_schema.load(request.get_json())
    response = jsonify(server.request.futures_change_leverage(**payload))
    return response


@blueprint.route("/margin-type", methods=["PUT"])
def margin_type() -> Response:
    server = get_server()
    payload = trade_put_margin_type_schema.load(request.get_json())
    response = jsonify(server.request.futures_change_margin_type(**payload))
    return response


@blueprint.route("/position-margin", methods=["GET", "PUT"])
def position_margin() -> Response:
    server = get_server()
    response = Response()

    if request.method == "GET":
        params = trade_get_position_margin_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_position_margin_history(**params))
    elif request.method == "PUT":
        payload = trade_put_position_margin_schema.load(request.get_json())
        response = jsonify(server.request.futures_change_position_margin(**payload))
    return response


@blueprint.route("/mode/position", methods=["GET", "PUT"])
def position_mode() -> Response:
    server = get_server()
    response = Response()

    if request.method == "GET":
        response = jsonify(server.request.futures_get_position_mode())
    elif request.method == "PUT":
        payload = trade_put_position_mode_schema.load(request.get_json())
        response = jsonify(server.request.futures_change_position_mode(**payload))
    return response


@blueprint.route("mode/multi-asset", methods=["GET", "PUT"])
def multi_assets_mode() -> Response:
    server = get_server()
    response = Response()

    if request.method == "GET":
        response = jsonify(server.request.futures_get_multi_assets_mode())
    elif request.method == "PUT":
        payload = trade_put_multi_asset_mode_schema.load(request.get_json())
        response = jsonify(server.request.futures_change_multi_assets_mode(**payload))
    return response
