from flask import render_template

from src.categorias import categoria
from src.db.Categorias import Categorias


# Crear los endpoints
# Ruta: http://127.0.0.1:5000/categorias/get
@categoria.route('/')
def get_categorias():
    obj = Categorias()
    print(obj.obtener_categorias())
    return render_template("categorias/index.html")
