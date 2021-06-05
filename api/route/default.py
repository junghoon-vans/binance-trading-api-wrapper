from flask import request, jsonify, Response

from api import get_server
from api.schema import time_schema, stream_schema
from api.spec import DocumentedBlueprint


blueprint = DocumentedBlueprint("default", __name__, url_prefix="/")


@blueprint.route("/ping", methods=["GET"])
def ping() -> Response:
    """
    Test Connectivity
    ---
    get:
      description: Test connectivity to the Rest API.
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    response = jsonify(server.request.futures_ping())
    return response


@blueprint.route("/time", methods=["GET"])
def time() -> Response:
    """
    Check Server Time
    ---
    get:
      description: Test connectivity to the Rest API and get the current server time.
      responses:
        200:
          content:
            application/json:
              schema: TimeSchema
          description: OK
    """
    server = get_server()
    response = jsonify(time_schema.dump(server.request.futures_time()))
    return response


@blueprint.route("/stream", methods=["GET"])
def stream() -> Response:
    """
    User Data Stream
    ---
    get:
      description: Generate a Listen Key
      responses:
        200:
          content:
            application/json:
              schema: StreamSchema
          description: OK
    """
    server = get_server()
    listen_key = server.request.futures_stream_get_listen_key()
    response = jsonify(stream_schema.dump({"listenKey": listen_key}))
    return response


@blueprint.route("/stream/<listen_key>", methods=["PUT", "DELETE"])
def modify_stream(listen_key) -> Response:
    """
    User Data Stream
    ---
    put:
      description: Ping/Keep-alive a Listen Key
      parameters:
        - in: path
          name: listenKey
      responses:
        200:
          content:
            application/json: {}
          description: OK
    delete:
      description: Close a ListenKey
      parameters:
        - in: path
          name: listenKey
      responses:
        200:
          content:
            application/json: {}
          description: OK
    """
    server = get_server()
    if request.method == "PUT":
        response = jsonify(
            server.request.futures_stream_keepalive(listenKey=listen_key)
        )
    elif request.method == "DELETE":
        response = jsonify(server.request.futures_stream_close(listenKey=listen_key))
    return response
