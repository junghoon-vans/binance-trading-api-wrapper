from flask import Blueprint, request

from api import get_server


blueprint = Blueprint("account", __name__, url_prefix="/account")


@blueprint.route("/account_transfer/")
def account_transfer():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_account_transfer(**params)


@blueprint.route("/transfer_history/")
def transfer_history():
    server = get_server()
    params = request.args.to_dict()
    return server.request.transfer_history(**params)


@blueprint.route("/account_balance/")
def account_balance():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_account_balance(**params)


@blueprint.route("/account/")
def account():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_account(**params)


@blueprint.route("/position_information/")
def position_information():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_position_information(**params)


@blueprint.route("/account_trades/")
def account_trades():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_account_trades(**params)


@blueprint.route("/income_history/")
def income_history():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_income_history(**params)


@blueprint.route("/leverage_bracket/")
def leverage_bracket():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_leverage_bracket(**params)
