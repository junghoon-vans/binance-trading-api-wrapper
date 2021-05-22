from typing import Any, Dict

from binance import Client


class MainnetClient(Client):
    def __init__(self, config: Dict[Any, Any]):
        super().__init__(**config)


class TestnetClient(Client):
    def __init__(self, config: Dict[Any, Any]):
        super().__init__(**config, testnet=True)
