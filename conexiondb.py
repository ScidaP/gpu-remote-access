# This Python file us-es the following encoding: utf-8

# if __name__ == "__main__":
#     pass

import psycopg2 as pgsql

class db:
    def __init__(self, dbname, user, password, host="localhost"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.conexion = ""

    def conectar(self):
        try:
            conexion = pgsql.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host
            )
            self.conexion = conexion;
        except Exception:
            print("Error al conectar la DB: %s", Exception.args)
    def coincide(self, usuario, contra):
        try:
            cursor = self.conexion.cursor()
            contra_s = str(contra)

            cursor.execute("SELECT * FROM usuarios WHERE usuario=%s AND password=%s", (usuario, contra_s))

            res = cursor.fetchone()

            if res:
                return True
            return False
        except Exception:
            return 'e'

"""
bd = db("ejemplo","admin","admin")
bd.conectar()
print(bd.coincide("Pato", 1234))
"""
