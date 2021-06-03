from flask import Blueprint, request, jsonify, Response

from api import get_server
from api.schema import (
    account_transfer_schema,
    account_transfer_history_schema,
    account_trades_schema,
    account_postion_info_schema,
    account_income_history_schema,
    account_leverage_bracket_schema,
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
        params = account_transfer_history_schema.load(request.args.to_dict())
        response = jsonify(server.request.transfer_history(**params))
    elif request.method == "POST":
        params = account_transfer_schema.load(request.args.to_dict())
        response = jsonify(server.request.futures_account_transfer(**params))
    return response


@blueprint.route("/trades", methods=["GET"])
def account_trades() -> Response:
    server = get_server()
    params = account_trades_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_account_trades(**params))
    return response


@blueprint.route("/position", methods=["GET"])
def position_information() -> Response:
    server = get_server()
    params = account_postion_info_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_position_information(**params))
    return response


@blueprint.route("/income", methods=["GET"])
def income_history() -> Response:
    server = get_server()
    params = account_income_history_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_income_history(**params))
    return response


@blueprint.route("/leverage-bracket", methods=["GET"])
def leverage_bracket() -> Response:
    server = get_server()
    params = account_leverage_bracket_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_leverage_bracket(**params))
    return response
