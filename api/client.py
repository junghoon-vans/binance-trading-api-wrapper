from binance import Client


class MainnetClient(Client):
    def __init__(self, api_key, api_secret):
        super().__init__(api_key, api_secret)


class TestnetClient(Client):
    def __init__(self, api_key, api_secret):
        super().__init__(api_key, api_secret, testnet=True)
