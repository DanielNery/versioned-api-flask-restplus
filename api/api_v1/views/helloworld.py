from flask import Blueprint
from flask_restplus import Api

from api.api_v2.resources.helloworld import HelloWorldResource


helloworld_resource_bp = Blueprint("v1_helloworld_resource", __name__, url_prefix="")

api = Api(helloworld_resource_bp)

helloworld_namespace = api.namespace(
    "regulacao", description="Dados relacionados a Regulação de Sinistro", path="/"
)


helloworld_namespace.add_resource(HelloWorldResource, f"/hello-world", methods=["GET"])
