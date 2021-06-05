from flask import request, jsonify, Response

from api import get_server
from api.schema import (
    account_get_transfer_schema,
    account_post_transfer_schema,
    account_get_trades_schema,
    account_get_postion_schema,
    account_get_income_schema,
    account_get_leverage_bracket_schema,
)
from api.spec import DocumentedBlueprint


blueprint = DocumentedBlueprint("account", __name__, url_prefix="/account")


@blueprint.route("/", methods=["GET"])
def account() -> Response:
    """
    Account Information
    ---
    get:
      description: Get current account information.
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    response = jsonify(server.request.futures_account())
    return response


@blueprint.route("/balance", methods=["GET"])
def balance() -> Response:
    """
    Futures Account Balance
    ---
    get:
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    response = jsonify(server.request.futures_account_balance())
    return response


@blueprint.route("/transfer", methods=["GET", "POST"])
def transfer() -> Response:
    """
    Futures Account Transfer
    ---
    get:
      description: Get Future Account Transaction History List.
      parameters:
        - in: query
          schema: GetTransferSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    post:
      description: New Future Account Transfer.
      requestBody:
        required: true
        content:
          application/json:
            schema: PostTransferSchema
      responses:
          200:
            content:
              application/json: {}
            description: OK
    """
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
def trades() -> Response:
    """
    Account Trade List
    ---
    get:
      description: Get trades for a specific account and symbol.
      parameters:
        - in: query
          schema: GetTradesSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = account_get_trades_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_account_trades(**params))
    return response


@blueprint.route("/position", methods=["GET"])
def position() -> Response:
    """
    Position Information
    ---
    get:
      description: Get current position information.
      parameters:
        - in: query
          schema: GetPositionSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = account_get_postion_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_position_information(**params))
    return response


@blueprint.route("/income", methods=["GET"])
def income() -> Response:
    """
    Get Income History
    ---
    get:
      parameters:
        - in: query
          schema: GetIncomeSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = account_get_income_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_income_history(**params))
    return response


@blueprint.route("/leverage-bracket", methods=["GET"])
def leverage_bracket() -> Response:
    """
    Notional and Leverage Brackets
    ---
    get:
      parameters:
        - in: query
          schema: GetLeverageBracketSchema
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    params = account_get_leverage_bracket_schema.load(request.args.to_dict())
    response = jsonify(server.request.futures_leverage_bracket(**params))
    return response
