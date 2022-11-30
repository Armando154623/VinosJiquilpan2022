import pymongo


class Connection:

    def __init__(self):
        self.DATABASE = "tienda"
        self.USER = 'armando1546'
        self.PASSWD = 'AccesoPermitido'
        self.MONGO_CLIENT = None
        self.MONGO_TIMEOUT = 1000
        self.MONGO_PETICION = F'mongodb+srv://{self.USER}:{self.PASSWD}@myfirstcluster.wtyy1eo.mongodb.net' \
                              F'/?retryWrites=true&w=majority '

    def abrir(self):
        conecto = False
        try:
            self.MONGO_CLIENT = pymongo.MongoClient(self.MONGO_PETICION)
            conecto = True
        except Exception as error:
            print("Error al abrir la conexion: ", error)
        return conecto

    def cerrar(self):
        if self.MONGO_CLIENT is not None:
            self.MONGO_CLIENT.close()

    def test(self):
        conecto = False
        try:
            self.MONGO_CLIENT = pymongo.MongoClient(self.MONGO_PETICION)
            self.MONGO_CLIENT.test()
            conecto = True
            self.MONGO_CLIENT.close()
        except Exception as error:
            print("Error: ", error)
        return conecto

    def get(self, table: str):
        return self.MONGO_CLIENT[self.DATABASE][table]
