from flask import Flask

from api.route import init_route
from api.spec import spec

app = Flask(__name__)
init_route(app)

print(spec.to_yaml())
