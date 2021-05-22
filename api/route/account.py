from flask import request
from flask_restful import Api, Resource

from api import get_server


def register_account_route(api: Api):
    api.add_resource(AccountTransfer, "/account_transfer")
    api.add_resource(TransferHistory, "/transfer_history")
    api.add_resource(AccountBalance, "/account_balance")
    api.add_resource(Account, "/account")
    api.add_resource(PositionInformation, "/position_information")
    api.add_resource(AccountTrades, "/account_trades")
    api.add_resource(IncomeHistory, "/income_history")
    api.add_resource(LeverageBracket, "/leverage_bracket")


class AccountTransfer(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_account_transfer(**params)


class TransferHistory(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.transfer_history(**params)


class AccountBalance(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_account_balance(**params)


class Account(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_account(**params)


class PositionInformation(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_position_information(**params)


class AccountTrades(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_account_trades(**params)


class IncomeHistory(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_income_history(**params)


class LeverageBracket(Resource):
    def get(self):
        server = get_server()
        params = request.args.to_dict()
        return server.request.futures_leverage_bracket(**params)
