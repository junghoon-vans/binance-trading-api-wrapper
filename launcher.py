import argparse

from api import get_server
from api.route import init_route


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="binance trading api launcher")
    parser.add_argument(
        "-a",
        "--address",
        type=str,
        default="0.0.0.0",
        help="ip address binding HTTP server",
    )
    parser.add_argument(
        "-p", "--port", type=int, default=5000, help="port number binding HTTP server"
    )
    parser.add_argument(
        "-e",
        "--environment",
        type=str,
        default="production",
        help="environment to running api server",
    )
    args = parser.parse_args()

    server = get_server(env=args.environment)
    init_route(server.app)
    server.app.run(args.address, args.port)
