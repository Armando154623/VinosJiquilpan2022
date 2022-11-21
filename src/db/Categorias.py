from src.db.Connection import Connection


class Categorias:
    con: Connection = None

    def __init__(self):
        self.con = Connection()

    def obtener_categorias(self):
        categorias = []
        if self.con.abrir():
            try:
                res = self.con.get("categorias").find({})
                for reg in res:
                    categorias.append(reg)
                self.con.cerrar()
            except Exception as error:
                print("Error en obtener_categorias: ", error)
        return categorias
