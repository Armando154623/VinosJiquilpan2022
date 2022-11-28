from flask import render_template, request

from src.db.Categorias import Categorias
from src.db.Productos import Productos
from src.productos import producto


@producto.route('/')
def get_productos():
    objProd = Productos()
    objCat = Categorias()

    if request.args.get("idCategoria") != None:
        filtro = {"$match": {"idCategoria.idCategoria": int(request.args.get("idCategoria"))}}
    else:
        filtro = {"$match": {}}

    campos = {"_id": 0,
              "idCategoria": 1,
              "nombreCategoria": 1,
              "imagenCategoria": 1,
              }

    categorias = objCat.obtener_categorias()

    campos = {"_id": 0,
              "idProducto": 1,
              "productoNombreCorto": 1,
              "productoTipo": 1,
              "productoImagen": 1,
              "idCategoria.nombreCategoriaProducto": 1,
              }

    productos = objProd.obtener_productos({}, campos)

    return render_template('product.html')
