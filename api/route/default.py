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


@blueprint.route("/stream/", methods=('GET', 'PUT', 'DELETE'))
def stream():
    server = get_server()
    if request.method == 'GET':
        return server.request.futures_stream_get_listen_key()
    elif request.method == 'PUT':
        listenKey = request.args.get("listenKey")
        return server.request.futures_stream_keepalive(listenKey=listenKey)
    elif request.method == 'DELETE':
        listenKey = request.args.get("listenKey")
        return server.request.futures_stream_close(listenKey=listenKey)
