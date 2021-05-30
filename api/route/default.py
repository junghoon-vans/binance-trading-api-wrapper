from flask import Blueprint, request, jsonify

from api import get_server
from api.schema import stream_schema


blueprint = Blueprint("default", __name__, url_prefix="/")


@blueprint.route("/ping")
def ping():
    server = get_server()
    response = server.request.futures_ping()
    return jsonify(response)


@blueprint.route("/time")
def time():
    server = get_server()
    response = server.request.futures_time()
    return jsonify(response)


@blueprint.route("/stream", methods=("GET", "PUT", "DELETE"))
def stream():
    server = get_server()
    response = {}

    if request.method == "GET":
        listen_key = server.request.futures_stream_get_listen_key()
        response = stream_schema.dump({"listenKey": listen_key})
    elif request.method == "PUT":
        payload = stream_schema.load(request.args.to_dict())
        listen_key = payload["listenKey"]
        response = server.request.futures_stream_keepalive(listenKey=listen_key)
    elif request.method == "DELETE":
        payload = stream_schema.load(request.args.to_dict())
        listen_key = payload["listenKey"]
        response = server.request.futures_stream_close(listenKey=listen_key)

    return jsonify(response)
