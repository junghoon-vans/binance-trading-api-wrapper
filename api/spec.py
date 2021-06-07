from typing import Callable

from flask import Blueprint

from apispec import APISpec, BasePlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

from api.utils.convert_case import camel_case, title_case


class DocumentedBlueprint(Blueprint):
    def __init__(self, name, import_name, **kwargs):
        super().__init__(name, import_name, **kwargs)
        self.view_funcs = []

    def add_url_rule(
        self,
        rule,
        endpoint=None,
        view_func=None,
        **kwargs,
    ):
        super().add_url_rule(
            rule,
            endpoint=endpoint,
            view_func=view_func,
            **kwargs,
        )
        self.view_funcs.append(view_func)

    def register(self, app, options):
        super().register(app, options)
        for view_func in self.view_funcs:
            spec.path(view=view_func, app=app, blueprint_name=self.name)


class DocPlugin(BasePlugin):
    def path_helper(
        self,
        operations: dict,
        view: Callable,
        path: str,
        blueprint_name: str,
        **kwargs,
    ):
        for method, operation in operations.items():
            function_name = view.__name__
            operation.setdefault(
                "operationId", camel_case(method + "_" + function_name)
            )
            operation.setdefault("summary", title_case(function_name))
            operation.setdefault("tags", []).append(blueprint_name)


spec = APISpec(
    title="binance-trading-api",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin(), DocPlugin()],
)
