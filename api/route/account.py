from flask import Blueprint, request, jsonify, Response

from api import get_server
from api.schema import (
    account_get_transfer_schema,
    account_post_transfer_schema,
    account_get_trades_schema,
    account_get_postion_schema,
    account_get_income_schema,
    account_get_leverage_bracket_schema,
)


blueprint = Blueprint("account", __name__, url_prefix="/account")


@blueprint.route("/", methods=["GET"])
def account() -> Response:
    server = get_server()
    response = jsonify(server.request.futures_account())
    return response


@blueprint.route("/balance", methods=["GET"])
def account_balance() -> Response:
    server = get_server()
    response = jsonify(server.request.futures_account_balance())
    return response


@blueprint.route("/transfer", methods=["GET", "POST"])
def transfer() -> Response:
    server = get_server()
    response = Response()

    if request.method == "GET":
        params = account_get_transfer_schema.load(request.args.to_dict())
        response = jsonify(server.request.transfer_history(**params))
    elif request.method == "POST":
        payload = account_post_transfer_schema.load(request.get_json())
        response = jsonify(server.request.futures_account_transfer(**payload))
    return response


@blueprint.route("/trades", methods=["GET"])
def account_trades() -> Response:
    server = get_server()
    params = account_get_trades_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_account_trades(**params))
    return response


@blueprint.route("/position", methods=["GET"])
def position_information() -> Response:
    server = get_server()
    params = account_get_postion_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_position_information(**params))
    return response


@blueprint.route("/income", methods=["GET"])
def income_history() -> Response:
    server = get_server()
    params = account_get_income_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_income_history(**params))
    return response


@blueprint.route("/leverage-bracket", methods=["GET"])
def leverage_bracket() -> Response:
    server = get_server()
    params = account_get_leverage_bracket_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_leverage_bracket(**params))
    return response
