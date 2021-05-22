from typing import Any, Dict

from binance import Client


class MainnetClient(Client):
    def __init__(self, network_config: Dict[Any, Any]):
        config = network_config.get("mainnet")
        super().__init__(**config)


class TestnetClient(Client):
    def __init__(self, network_config: Dict[Any, Any]):
        config = network_config.get("testnet")
        super().__init__(**config, testnet=True)
