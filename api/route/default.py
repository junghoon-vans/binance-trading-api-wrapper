from flask import Blueprint, request, jsonify, Response

from api import get_server
from api.schema import ping_schema, time_schema, stream_schema


blueprint = Blueprint("default", __name__, url_prefix="/")


@blueprint.route("/ping")
def ping() -> Response:
    server = get_server()
    response = jsonify(ping_schema.dump(server.request.futures_ping()))
    return response


@blueprint.route("/time")
def time() -> Response:
    server = get_server()
    response = jsonify(time_schema.dump(server.request.futures_time()))
    return response


@blueprint.route("/stream", methods=("GET", "PUT", "DELETE"))
def stream() -> Response:
    server = get_server()
    response = Response()

    if request.method == "GET":
        listen_key = server.request.futures_stream_get_listen_key()
        response = jsonify(stream_schema.dump({"listenKey": listen_key}))
    elif request.method == "PUT":
        payload = stream_schema.load(request.args.to_dict())
        listen_key = payload["listenKey"]
        response = jsonify(
            server.request.futures_stream_keepalive(listenKey=listen_key)
        )
    elif request.method == "DELETE":
        payload = stream_schema.load(request.args.to_dict())
        listen_key = payload["listenKey"]
        response = jsonify(server.request.futures_stream_close(listenKey=listen_key))

    return response
