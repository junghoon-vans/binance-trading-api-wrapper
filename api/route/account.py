from flask import Blueprint, request, jsonify

from api import get_server


blueprint = Blueprint("account", __name__, url_prefix="/account")


@blueprint.route("/")
def account():
    server = get_server()
    response = server.request.futures_account()

    return jsonify(response)


@blueprint.route("/balance")
def account_balance():
    server = get_server()
    response = server.request.futures_account_balance()

    return jsonify(response)


@blueprint.route("/transfer", methods=("GET", "POST"))
def transfer():
    server = get_server()
    params = request.args.to_dict()
    response = {}

    if request.method == "POST":
        response = server.request.futures_account_transfer(**params)
    elif request.method == "GET":
        response = server.request.transfer_history(**params)

    return jsonify(response)


@blueprint.route("/trades")
def account_trades():
    server = get_server()
    symbol = request.args.get("symbol")
    response = server.request.futures_account_trades(symbol=symbol)

    return jsonify(response)


@blueprint.route("/position")
def position_information():
    server = get_server()
    symbol = request.args.get("symbol")
    response = server.request.futures_position_information(symbol=symbol)

    return jsonify(response)


@blueprint.route("/income")
def income_history():
    server = get_server()
    params = request.args.to_dict()
    response = server.request.futures_income_history(**params)

    return jsonify(response)


@blueprint.route("/leverage-bracket")
def leverage_bracket():
    server = get_server()
    symbol = request.args.get("symbol")
    response = server.request.futures_leverage_bracket(symbol=symbol)

    return jsonify(response)
