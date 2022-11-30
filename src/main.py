from flask import render_template


from src import create_app
from src.db.Categorias import Categorias
from src.db.Productos import Productos
from src.db.mongodb import PyMongo

app = create_app()


# @app.route('/')
# def index():
#     objProd = Productos()
#     objCat = Categorias()
#
#     campos = {"_id": 0,
#               "idCategoria": 1,
#               "nombreCategoria": 1,
#               "imagenCategoria": 1
#     }
#     categorias = objCat.obtener_categorias({}, campos)
#
#     campos = {
#         "_id": 0,
#         "idProducto": 1,
#         "productoNombreCorto": 1,
#         "productoTipo": 1,
#         "productoImagen": 1,
#         "idCategoria.nombreCategoriaProducto": 1
#     }
#     productos = objProd.obtener_productos()
#
#     print(categorias)
#     print(productos)
#
#     return render_template('index.html',
#                            categorias=categorias,
#                            productos=productos["resultado"])  # 'OK'

@app.route('/')
def index():
    # Abrir BAse de Datos
    objPyMongo = PyMongo()
    # Consultar
    objPyMongo.conectar_mongodb()
    campos = {"_id": 0,
              "idCategoria": 1,
              "nombreCategoria": 1,
              "imagenCategoria": 1}
    lista_categorias = objPyMongo.consulta_mongodb('categorias', {}, campos)
    campos = {
        "_id": 0,
        "idProducto": 1,
        "productoNombreCorto": 1,
        "productoTipo": 1,
        "productoImagen": 1,
        "idCategoria.nombreCategoriaProducto": 1
    }
    lista_productos = objPyMongo.consulta_general_productos('productos')
    # Cerrar la conexion
    objPyMongo.desconectar_mongodb()
    # Imprimir categorias
    print(lista_categorias)
    print(lista_productos)
    # Regresamos categorias
    return render_template('index.html',
                           categorias=lista_categorias["resultado"],
                           productos=lista_productos["resultado"])  # 'OK'