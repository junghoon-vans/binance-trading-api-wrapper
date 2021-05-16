from typing import Any, Dict

from binance_f import RequestClient


class MainnetClient(RequestClient):
    def __init__(self, network_config: Dict[Any, Any]):
        config = network_config.get("mainnet")
        super().__init__(**config)


class TestnetClient(RequestClient):
    def __init__(self, network_config: Dict[Any, Any]):
        config = network_config.get("testnet")
        super().__init__(**config)
