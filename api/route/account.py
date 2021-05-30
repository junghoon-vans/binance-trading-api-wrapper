from flask import Blueprint, request, jsonify, Response

from api import get_server


blueprint = Blueprint("account", __name__, url_prefix="/account")


@blueprint.route("/")
def account() -> Response:
    server = get_server()
    response = jsonify(server.request.futures_account())
    return response


@blueprint.route("/balance")
def account_balance() -> Response:
    server = get_server()
    response = jsonify(server.request.futures_account_balance())
    return response


@blueprint.route("/transfer", methods=("GET", "POST"))
def transfer() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = Response()

    if request.method == "POST":
        response = jsonify(server.request.futures_account_transfer(**params))
    elif request.method == "GET":
        response = jsonify(server.request.transfer_history(**params))
    return response


@blueprint.route("/trades")
def account_trades() -> Response:
    server = get_server()
    symbol = request.args.get("symbol")
    response = jsonify(server.request.futures_account_trades(symbol=symbol))
    return response


@blueprint.route("/position")
def position_information() -> Response:
    server = get_server()
    symbol = request.args.get("symbol")
    response = jsonify(server.request.futures_position_information(symbol=symbol))
    return response


@blueprint.route("/income")
def income_history() -> Response:
    server = get_server()
    params = request.args.to_dict()
    response = jsonify(server.request.futures_income_history(**params))
    return response


@blueprint.route("/leverage-bracket")
def leverage_bracket() -> Response:
    server = get_server()
    symbol = request.args.get("symbol")
    response = jsonify(server.request.futures_leverage_bracket(symbol=symbol))
    return response
