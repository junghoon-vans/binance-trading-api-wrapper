from flask import Blueprint

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

spec = APISpec(
    title="binance-trading-api",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


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
            spec.path(view=view_func, app=app)
