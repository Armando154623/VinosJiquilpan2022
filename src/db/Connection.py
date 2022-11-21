import pymongo


class Connection:

    def __init__(self):
        self.DATABASE = "itj_estudiantes"
        self.USER = 'armando1546'
        self.PASSWD = 'AccesoPermitido'
        self.MONGO_CLIENT = None
        self.MONGO_TIMEOUT = 1000
        self.MONGO_PETICION = F'mongodb+srv://{self.USER}:{self.PASSWD}@myfirstcluster.wtyy1eo.mongodb.net/?retryWrites=true&w=majority'

    def abrir(self):
        conecto = False
        try:
            self.MONGO_CLIENT = pymongo.MongoClient(self.MONGO_PETICION)
            conecto = True
        except Exception as error:
            print("Error: ", error)
        return conecto

    def cerrar(self):
        if self.MONGO_CLIENT is not None:
            self.MONGO_CLIENT.close()

    def test(self):
        conecto = False
        try:
            self.MONGO_CLIENT = pymongo.MongoClient(self.MONGO_PETICION)
            conecto = True
            self.MONGO_CLIENT.close()
        except Exception as error:
            print("Error: ", error)
        return conecto

    def get(self, table: str):
        return self.MONGO_CLIENT[self.DATABASE][table]

    # def consulta_mongo(self, tabla: str, busqueda: dict, filtro: dict = None):
    #     resultado = []
    #     if self.abrir():
    #         try:
    #             if filtro is None:
    #                 res = self.MONGO_CLIENT[self.DATABASE][tabla].find(busqueda)
    #             else:
    #                 res = self.MONGO_CLIENT[self.DATABASE][tabla].find(busqueda, filtro)
    #             for reg in res:
    #                 resultado.append(reg)
    #
    #             self.cerrar()
    #         except Exception as error:
    #             print("Error en la consulta: ", error)
    #     return resultado
    #
    # def insertar_mongo(self, tabla: str, insertar: dict):
    #     res = None
    #     if self.abrir():
    #         try:
    #             res = self.MONGO_CLIENT[self.DATABASE][tabla].insert_one(insertar)
    #             self.cerrar()
    #         except Exception as error:
    #             print("Error en la consulta: ", error)
    #     return res
    #
    # def insertar_varios(self, tabla: str, document: list):
    #     res = None
    #     if self.abrir():
    #         try:
    #             res = self.MONGO_CLIENT[self.DATABASE][tabla].insert_many(document)
    #             self.cerrar()
    #         except Exception as error:
    #             print("Error en la consulta: ", error)
    #     return res
    #
    # def modificar_mongo(self, tabla: str, consulta: dict, valores: dict):
    #     res = None
    #     if self.abrir():
    #         try:
    #             res = self.MONGO_CLIENT[self.DATABASE][tabla].update_one(consulta, valores)
    #             self.cerrar()
    #         except Exception as error:
    #             print("Error en la consulta: ", error)
    #     return res
    #
    # def eliminar_mongo(self, tabla: str, consulta: dict = None):
    #     res = None
    #     if self.abrir():
    #         try:
    #             if consulta is None:
    #                 res = self.MONGO_CLIENT[self.DATABASE][tabla].drop()
    #             else:
    #                 res = self.MONGO_CLIENT[self.DATABASE][tabla].delete_one(consulta)
    #             self.cerrar()
    #         except Exception as error:
    #             print("Error en la consulta: ", error)
    #     return res
    #
    # def eliminar_mongo_varios(self, tabla: str, campo, condicion):
    #     res = None
    #     if self.abrir():
    #         try:
    #             res = self.MONGO_CLIENT[self.DATABASE][tabla].delete_many({campo: {"$regex": condicion}})
    #             self.cerrar()
    #         except Exception as error:
    #             print("Error en la consulta: ", error)
    #     return res