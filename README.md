Binance Trading API Wrapper
===

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Jeonghun-Ban/binance-trading-api-wrapper/Deploy%20API%20docs?style=flat-square)

About
---

This project is for futures trading on Binance by api call such as tradingview strategy alert. For this, I used [python-binance](https://github.com/sammchardy/python-binance). Detailed information related to the package can be found through [this document page](https://python-binance.readthedocs.io/en/latest/index.html#).

Usage
---

### Clone this project

```bash
git clone https://github.com/Jeonghun-Ban/binance-trading-api-wrapper.git
```

### Install dependency packages

```bash
pip install -r requirements.txt
```

### Configuration

#### 1. config files

Configuration files using `YAML` format are in [/configs](/configs).

```
cp example.toml production.toml
cp example.toml development.toml
cp example.toml testing.toml
```

You can easily create `config files` by copying [example.toml](/configs/example.toml). 

#### 2. Environment variable

Register `api key`, `secret key` in `environment variable` for accessing binance network before running on the server.

- BINANCE_TESTNET_API_KEY
- BINANCE_TESTNET_SECRET_KEY
- BINANCE_MAINNET_API_KEY
- BINANCE_MAINNET_SECRET_KEY

The environment variable name is set as above.

> if you only access mainnet, you don't need to register testnet keys.

### Start launcher

```bash
python launcher [-h][-a][-p][-e] # help, address, port, environment
python launcher -e development # run server with development env
python launcher -e testing # run server with testing env
```

`launcher.py` runs with `address=0.0.0.0`, `port=5000`, `environment=production` if there are no arguments.

> The testing environment connects to the Binance testnet. Therefore, you need to set `api_key`, `api_secret` as `environment variable` before executing server.


### Build apidocs pages

```
python apidocs.py > openapi.yaml
redoc-cli bundle openapi.yaml -o ./publish/index.html
```

> This requires a `redoc-cli` installation. 

Components
---

```
.
├── api
│   ├── route
│   │   └── __init__.py
│   │   └── account.py
│   │   └── default.py
│   │   └── market.py
│   │   └── trade.py
│   ├── schema
│   │   └── __init__.py
│   │   └── base.py
│   │   └── account.py
│   │   └── default.py
│   │   └── market.py
│   │   └── trade.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── convert_case.py
│   ├── __init__.py
│   ├── client.py
│   └── enum.py
│   └── spec.py
├── configs
│   └── development.toml
│   └── example.toml
│   └── production.toml
│   └── testing.toml
├── .gitignore
├── .pre-commit-config.yaml
├── apidocs.py
├── launcher.py
├── README.md
├── requirements.txt
└── setup.cfg
```
