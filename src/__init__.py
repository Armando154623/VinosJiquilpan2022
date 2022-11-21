from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    from src.categorias import categoria
    app.register_blueprint(categoria)

    from src.productos import producto
    app.register_blueprint(producto)

    app.config.from_object('config.DevConfig')

    CORS(app)

    return app
