from flask import request, jsonify, Response

from api import get_server
from api.schema import ping_schema, time_schema, stream_schema
from api.spec import DocumentedBlueprint


blueprint = DocumentedBlueprint("default", __name__, url_prefix="/")


@blueprint.route("/ping", methods=["GET"])
def ping() -> Response:
    server = get_server()
    response = jsonify(ping_schema.dump(server.request.futures_ping()))
    return response


@blueprint.route("/time", methods=["GET"])
def time() -> Response:
    server = get_server()
    response = jsonify(time_schema.dump(server.request.futures_time()))
    return response


@blueprint.route("/stream", methods=["GET"])
def stream() -> Response:
    server = get_server()
    listen_key = server.request.futures_stream_get_listen_key()
    response = jsonify(stream_schema.dump({"listenKey": listen_key}))
    return response


@blueprint.route("/stream/<listen_key>", methods=["PUT", "DELETE"])
def modify_stream(listen_key) -> Response:
    server = get_server()
    if request.method == "PUT":
        response = jsonify(
            server.request.futures_stream_keepalive(listenKey=listen_key)
        )
    elif request.method == "DELETE":
        response = jsonify(server.request.futures_stream_close(listenKey=listen_key))
    return response
