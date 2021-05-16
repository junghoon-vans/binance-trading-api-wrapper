import argparse

from api import get_server
from api.route import binding_route


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
        "-n",
        "--network",
        type=str,
        default="mainnet",
        help="select mainnet or testnet as spot network",
    )
    args = parser.parse_args()

    server = get_server(network=args.network)
    binding_route(server.api)
    server.app.run(args.address, args.port)
