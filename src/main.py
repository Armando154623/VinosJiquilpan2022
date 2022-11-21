from flask import render_template, Flask
from flask_cors import CORS

app = Flask(__name__)

from src.categorias import categoria
app.register_blueprint(categoria)

from src.productos import producto
app.register_blueprint(producto)

app.config.from_object('config.DevConfig')

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')
