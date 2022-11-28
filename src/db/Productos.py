from src.db.Connection import Connection


class Productos:
    con: Connection = None

    def __init__(self):
        self.con = Connection()

    def obtener_productos(self, filtro_registro=None, atributos=None):
        lista_pipelines = []
        response = {"status": False, "resultado": []}
        if self.con.abrir():
            try:
                filtro = {
                    "$match": {
                        "productoTipo": {'$ne': 1}
                    }
                }
                proyeccion = {
                    "$project": {
                        '_id': 0,
                        'idCategoria': "$idCategoria.idCategoria",
                        'nombreCategoria': "$idCategoria.nombreCategoriaProducto",
                        'idProducto': 1,
                        'productoTipo': 1,
                        'productoImagen': 1,
                        'productoCosto': 1,
                        'precioVenta':
                            {
                                "$subtract": [{
                                    "$add": [
                                        {
                                            "$multiply": [
                                                '$productoCosto',
                                                {"$divide": ['$productoGanancia', 100]}
                                            ]
                                        },
                                        '$productoCosto'
                                    ]
                                },
                                    {
                                        "$multiply": [
                                            '$productoCosto',
                                            {"$divide": ['$productoDescuento', 100]}
                                        ]
                                    }]
                            },
                        'descuento': {
                            "$multiply": [
                                '$productoCosto',
                                {"$divide": ['$productoDescuento', 100]}
                            ]
                        }
                    }
                }

                if filtro_registro is None:
                    lista_pipelines.append(filtro)
                else:
                    lista_pipelines.append(filtro_registro)

                lista_pipelines.append(proyeccion)

                res = self.con.get("productos").aggregate(lista_pipelines)

                if res:
                    response["status"] = True
                    for reg in res:
                        response["resultado"].append(reg)

                self.con.cerrar()
            except Exception as error:
                print("Error en obtener_productos: ", error)
        return response
