from flask import Blueprint, request

from api import get_server


blueprint = Blueprint("trade", __name__, url_prefix="/trade")


@blueprint.route("/order", methods=["GET", "POST", "DELETE"])
def order():
    params = request.args.to_dict()
    server = get_server()
    if request.method == "POST":
        server.request.futures_create_order(**params)
    elif request.method == "GET":
        server.request.futures_get_order(**params)
    elif request.method == "DELETE":
        server.request.futures_cancel_order(**params)


@blueprint.route("/order/multiple", methods=["POST", "DELETE"])
def mutiple_orders():
    params = request.args.to_dict()
    server = get_server()
    if request.method == "POST":
        server.request.futures_place_batch_order(**params)
    elif request.method == "DELETE":
        server.request.futures_cancel_orders(**params)


@blueprint.route("/order/open")
def get_open_orders():
    params = request.args.to_dict()
    server = get_server()
    server.request.futures_get_open_orders(**params)


@blueprint.route("/order/all", methods=["GET", "DELETE"])
def all_orders():
    params = request.args.to_dict()
    server = get_server()
    if request.method == "GET":
        server.request.futures_get_all_orders(**params)
    elif request.method == "DELETE":
        server.request.futures_cancel_all_open_orders(**params)


@blueprint.route("/leverage", methods=["POST"])
def change_leverage():
    if request.method == "POST":
        params = request.args.to_dict()
        server = get_server()
        return server.request.futures_change_leverage(**params)


@blueprint.route("/margin-type", methods=["POST"])
def change_margin_type():
    if request.method == "POST":
        params = request.args.to_dict()
        server = get_server()
        return server.request.futures_change_margin_type(**params)


@blueprint.route("/position-margin", methods=["GET", "POST"])
def position_margin():
    params = request.args.to_dict()
    server = get_server()
    if request.method == "GET":
        return server.request.futures_position_margin_history(**params)
    elif request.method == "POST":
        return server.request.futures_change_position_margin(**params)


@blueprint.route("/mode/position", methods=["GET", "POST"])
def position_mode():
    params = request.args.to_dict()
    server = get_server()
    if request.method == "GET":
        return server.request.futures_get_position_mode(**params)
    elif request.method == "POST":
        return server.request.futures_change_position_mode(**params)


@blueprint.route("mode/multi-asset", methods=["GET", "POST"])
def change_multi_assets_mode():
    params = request.args.to_dict()
    server = get_server()
    if request.method == "GET":
        return server.request.futures_get_multi_assets_mode()
    elif request.method == "POST":
        return server.request.futures_change_multi_assets_mode(**params)
