import argparse

from app import binding_api, get_server


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="binance trading bot launcher")
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

    server = get_server(args.network)
    binding_api(server)
    server.run(args.address, args.port)
