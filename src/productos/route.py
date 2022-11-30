from flask import render_template, request
from src.db.Categorias import Categorias
from src.db.Productos import Productos
from src.db.mongodb import PyMongo
from src.productos import producto


# @producto.route('/')
# def get_productos():
#     objProd = Productos()
#     objCat = Categorias()
#
#     if request.args.get("idCategoria") is not None:
#         filtro = {"$match": {"idCategoria.idCategoria": int(request.args.get("idCategoria"))}}
#     else:
#         filtro = {}
#
#     campos = {"_id": 0,
#               "idCategoria": 1,
#               "nombreCategoria": 1,
#               "imagenCategoria": 1
#               }
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
#     productos = objProd.obtener_productos(filtro)
#
#     print(categorias)
#     print(productos)
#
#     return render_template('productos/index.html',
#                            categorias=categorias["resultado"],
#                            productos=productos["resultado"])  # 'OK'


@producto.route('/')
def index_productos(): # get_productos() idProducto, Nombre, Imagen
    # Leer lo que traemos en la cadena de consulta

    print("ID: ", request.args.get('idCategoria'))
    if request.args.get('idCategoria') != None:
        filtro = {
                    "$match": { 'idCategoria.idCategoria': int(request.args.get('idCategoria')) }
                 }  #  {'idCategoria.idCategoria': int(request.args.get('idCategoria')) }
    else:
        filtro = { "$match": {  } }  #'productoTipo':{'$ne': 1}
    # Abrir BAse de Datos
    objPyMongo = PyMongo()
    # Consultar
    objPyMongo.conectar_mongodb()
    campos = {"_id":0,
              "idCategoria":1,
              "nombreCategoria":1,
              "imagenCategoria": 1}
    lista_categorias = objPyMongo.consulta_mongodb('categorias',{},campos)
    campos = {
        "_id": 0,
        "idProducto": 1,
        "productoNombreCorto": 1,
        "productoTipo": 1,
        "productoImagen": 1,
        "idCategoria.nombreCategoriaProducto": 1
    }
    lista_productos = objPyMongo.consulta_general_productos('productos',filtro) #{'productoTipo':{'$ne':1}}
    # Cerrar la conexion
    objPyMongo.desconectar_mongodb()
    # Imprimir categorias
    print(lista_categorias)
    print(lista_productos)
    # Regresamos categorias
    return render_template('productos/index.html',
                           categorias=lista_categorias["resultado"],
                           productos=lista_productos["resultado"] ) # 'OK'
