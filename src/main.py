from flask import render_template


from src import create_app
from src.db.Categorias import Categorias
from src.db.Productos import Productos

app = create_app()


@app.route('/')
def index():
    objProd = Productos()
    objCat = Categorias()
    campos = {"_id": 0,
              "idCategoria": 1,
              "nombreCategoria": 1,
              "imagenCategoria": 1}
    lista_categorias = objCat.obtener_categorias()
    campos = {
        "_id": 0,
        "idProducto": 1,
        "productoNombreCorto": 1,
        "productoTipo": 1,
        "productoImagen": 1,
        "idCategoria.nombreCategoriaProducto": 1
    }
    lista_productos = objProd.obtener_productos()
    # Imprimir categorias
    print(lista_categorias)
    print(lista_productos)
    # Regresamos categorias
    return render_template('index.html',
                           categorias=lista_categorias,
                           productos=lista_productos["resultado"])  # 'OK'

