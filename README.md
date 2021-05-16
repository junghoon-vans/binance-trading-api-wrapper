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

### Configuration

configuration files using `YAML` format are in [/configs](/configs).

```
cp example.yaml production.yaml
cp example.yaml development.yaml
cp example.yaml testing.yaml
```

you can easily create `config files` by copying [example.yaml](/configs/example.yaml). before running on the server, you need to set `api_key` and `secret_key` first.

### Start launcher

```bash
python launcher [-h][-a][-p][-n][-f] # help, address, port, network, filename
python launcher -n testnet # run server with testnet
python launcher -f development # apply development.yaml to configure file
```

`launcher.py` runs with `address=0.0.0.0`, `port=5000`, `network=mainnet`, `filename=production` if there are no arguments.

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
│   └── development.yaml
│   └── example.yaml
│   └── production.yaml
│   └── testing.yaml
├── .gitignore
├── .gitmodules
├── .pre-commit-config.yaml
├── launcher.py
├── README.md
├── requirements.txt
└── setup.cfg
```
