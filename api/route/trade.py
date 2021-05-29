from flask import Blueprint, request, jsonify

from api import get_server


blueprint = Blueprint("trade", __name__, url_prefix="/trade")


@blueprint.route("/order", methods=["GET", "POST", "DELETE"])
def order():
    server = get_server()
    params = request.args.to_dict()
    result = []

    if request.method == "GET":
        result = server.request.futures_get_order(**params)
    elif request.method == "POST":
        result = server.request.futures_create_order(**params)
    elif request.method == "DELETE":
        result = server.request.futures_cancel_order(**params)

    return jsonify(result)


@blueprint.route("/order/multiple", methods=["POST", "DELETE"])
def mutiple_orders():
    server = get_server()
    params = request.args.to_dict()
    result = []

    if request.method == "POST":
        result = server.request.futures_place_batch_order(**params)
    elif request.method == "DELETE":
        result = server.request.futures_cancel_orders(**params)

    return jsonify(result)


@blueprint.route("/order/open")
def get_open_orders():
    server = get_server()
    params = request.args.to_dict()

    return jsonify(server.request.futures_get_open_orders(**params))


@blueprint.route("/order/all", methods=["GET", "DELETE"])
def all_orders():
    server = get_server()
    params = request.args.to_dict()
    result = []

    if request.method == "GET":
        result = server.request.futures_get_all_orders(**params)
    elif request.method == "DELETE":
        result = server.request.futures_cancel_all_open_orders(**params)

    return jsonify(result)


@blueprint.route("/leverage", methods=["POST"])
def change_leverage():
    server = get_server()
    params = request.args.to_dict()
    result = server.request.futures_change_leverage(**params)

    return jsonify(result)


@blueprint.route("/margin-type", methods=["POST"])
def change_margin_type():
    server = get_server()
    params = request.args.to_dict()
    result = server.request.futures_change_margin_type(**params)

    return jsonify(result)


@blueprint.route("/position-margin", methods=["GET", "POST"])
def position_margin():
    server = get_server()
    params = request.args.to_dict()
    result = []

    if request.method == "GET":
        result = server.request.futures_position_margin_history(**params)
    elif request.method == "POST":
        result = server.request.futures_change_position_margin(**params)

    return jsonify(result)


@blueprint.route("/mode/position", methods=["GET", "POST"])
def position_mode():
    server = get_server()
    params = request.args.to_dict()
    result = []

    if request.method == "GET":
        result = server.request.futures_get_position_mode(**params)
    elif request.method == "POST":
        result = server.request.futures_change_position_mode(**params)

    return jsonify(result)


@blueprint.route("mode/multi-asset", methods=["GET", "POST"])
def change_multi_assets_mode():
    server = get_server()
    params = request.args.to_dict()
    result = []

    if request.method == "GET":
        result = server.request.futures_get_multi_assets_mode()
    elif request.method == "POST":
        result = server.request.futures_change_multi_assets_mode(**params)

    return jsonify(result)
