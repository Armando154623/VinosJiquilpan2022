from src.db.Connection import Connection


class Categorias:
    con: Connection = None

    def __init__(self):
        self.con = Connection()

    def obtener_categorias(self, filtro=None, atributos=None):
        response = {"status": False, "resultado": []}
        if self.con.abrir():
            try:
                if atributos is None:
                    atributos = {"_id": 0}
                if filtro is None:
                    filtro = {}

                res = self.con.get("categorias").find(filtro, atributos)

                if res:
                    response["status"] = True
                    for reg in res:
                        response["resultado"].append(reg)

                self.con.cerrar()
            except Exception as error:
                print("Error en obtener_categorias: ", error)
        return response
