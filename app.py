from flask import Flask
from api.api_v1.views.helloworld import (
    helloworld_resource_bp as v1_helloworld_resource_bp,
)
from api.api_v2.views.helloworld import (
    helloworld_resource_bp as v2_helloworld_resource_bp,
)

app = Flask(__name__)
app.register_blueprint(v1_helloworld_resource_bp, url_prefix="/api/v1")
app.register_blueprint(v2_helloworld_resource_bp, url_prefix="/api/v2")
app.run(debug=True)
