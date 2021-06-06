import argparse

from json import dumps as json_dump
from yaml import dump as yaml_dump
from apispec.yaml_utils import YAMLDumper

from flask import Flask

from api.route import init_route
from api.spec import spec


parser = argparse.ArgumentParser(description="API docs builder")
parser.add_argument(
    "-j",
    "--json",
    action="store_true",
)


def main():
    app = Flask(__name__)
    init_route(app)

    args = parser.parse_args()
    if args.json:
        print(json_dump(spec.to_dict(), ensure_ascii=False))
    else:
        print(yaml_dump(spec.to_dict(), Dumper=YAMLDumper, allow_unicode=True))


if __name__ == "__main__":
    main()
