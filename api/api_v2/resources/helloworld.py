from flask_restplus import Resource


class HelloWorldResource(Resource):
    def get(self):
        return "Hello World Versão 1"
