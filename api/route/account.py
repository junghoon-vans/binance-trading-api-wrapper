from flask import Blueprint, request, jsonify

from api import get_server


blueprint = Blueprint("account", __name__, url_prefix="/account")


@blueprint.route("/")
def account():
    server = get_server()
    return jsonify(
        server.request.futures_account()
    )


@blueprint.route("/balance/")
def account_balance():
    server = get_server()
    return jsonify(
        server.request.futures_account_balance()
    )


@blueprint.route("/transfer/", methods=('GET', 'POST'))
def transfer():
    params = request.args.to_dict()
    server = get_server()
    if request.method == 'POST':
        return jsonify(
            server.request.futures_account_transfer(**params)
        )
    elif request.method == 'GET':
        return jsonify(
            server.request.transfer_history(**params)
        )


@blueprint.route("/trades/")
def account_trades():
    symbol = request.args.get('symbol')
    server = get_server()
    return jsonify(
        server.request.futures_account_trades(symbol=symbol)
    )


@blueprint.route("/position/")
def position_information():
    symbol = request.args.get('symbol')
    server = get_server()
    return jsonify(
        server.request.futures_position_information(symbol=symbol)
    )


@blueprint.route("/income/")
def income_history():
    params = request.args.to_dict()
    server = get_server()
    return jsonify(
        server.request.futures_income_history(**params)
    )


@blueprint.route("/leverage-bracket/")
def leverage_bracket():
    symbol = request.args.get('symbol')
    server = get_server()
    return jsonify(
        server.request.futures_leverage_bracket(symbol=symbol)
    )
