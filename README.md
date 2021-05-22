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
python launcher [-h][-a][-p][-e] # help, address, port, environment
python launcher -e development # run server with development env
python launcher -e testing # run server with testing env
```

`launcher.py` runs with `address=0.0.0.0`, `port=5000`, `environment=production` if there are no arguments.

> The testing environment connects to the Binance testnet. Therefore, you need to set `api_key`, `api_secret` in the configuration file before executing server.

Components
---

```
.
├── api
│   ├── docs
│   │   └── change_leverage.yml
│   │   └── change_margin_type.yml
│   │   └── post_order.yml
│   ├── route
│   │   └── __init__.py
│   │   └── trade.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── config_proxy.py
│   ├── __init__.py
│   ├── client.py
│   └── environment.py
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

About
---

This project is for trading on Binance by triggering an alarm in the Trading View strategy. For this, I used [python-binance](https://github.com/sammchardy/python-binance). Detailed information related to the package can be found through [this document page](https://python-binance.readthedocs.io/en/latest/index.html#).