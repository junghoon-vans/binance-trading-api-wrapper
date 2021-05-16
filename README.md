Tradingview Binance Trading API
===

Usage
---

### Clone this project

```bash
git clone https://github.com/Jeonghun-Ban/tradingview-binance-trading-api.git
git submodule update --init --recursive # download submodule source code
```

### Install dependency packages

```bash
cd api/lib/binance-futures/
python setup.py install # binance-futures package
cd ....
pip install -r requirements.txt
```

### configs

config files formmated in `.yaml` are in [/configs](/configs).

```
cp example.yaml default.yaml
```

you can easily create `default.yaml` by copying [example.yaml](/configs/example.yaml). before running on the server, you need to set `api_key` and `secret_key` first.

### Start launcher

```bash
python launcher [-h][-a][-p][-n] # help, address, port, network
python launcher -n testnet
```

`launcher.py` runs with `address=0.0.0.0`, `port=5000`, `network=mainnet` if there are no arguments.

Components
---

```
.
├── api
│   ├── lib
│   │   └── binance-futures
│   │   └── __init__.py
│   ├── route
│   │   ├── __init__.py
│   │   └── trade.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── config_proxy.py
│   ├── __init__.py
│   ├── network.py
│   └── request_client.py
├── configs
│   └── example.yaml
├── .gitignore
├── .gitmodules
├── .pre-commit-config.yaml
├── launcher.py
├── README.md
├── requirements.txt
└── setup.cfg
```
