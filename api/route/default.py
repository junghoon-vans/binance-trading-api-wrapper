from flask import Blueprint, request

from api import get_server


blueprint = Blueprint("default", __name__, url_prefix="/")


@blueprint.route("/ping/")
def ping():
    server = get_server()
    return server.request.futures_ping()


@blueprint.route("/time/")
def time():
    server = get_server()
    return server.request.futures_time()


@blueprint.route("/exchange_info/")
def exchange_info():
    server = get_server()
    return server.request.futures_exchange_info()


@blueprint.route("/stream_get_listen_key/")
def stream_get_listen_key():
    server = get_server()
    return server.request.futures_stream_get_listen_key()


@blueprint.route("/stream_keepalive/")
def stream_keepalive():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_stream_keepalive(**params)


@blueprint.route("/stream_close/")
def futures_stream_close():
    server = get_server()
    params = request.args.to_dict()
    return server.request.futures_stream_close(**params)
