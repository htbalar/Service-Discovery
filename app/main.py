from flask import Flask
from flask_restx import Api
from controllers.service_discovery_controller import service_discovery_ns

def create_app():
    app = Flask(__name__)

    api = Api(app, title="Microservice Service Discovery", version="1.0", doc="/docs")
    app.register_blueprint(service_discovery_ns, url_prefix="/service-discovery")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
