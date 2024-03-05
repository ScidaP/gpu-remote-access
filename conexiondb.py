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
        conexion = pgsql.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host
        )
        self.conexion = conexion;

    def coincide(self, usuario, contra):
        cursor = self.conexion.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE usuario=%s AND password=%s", (usuario, contra))

        res = cursor.fetchone()

        if res:
            return True
        return False
