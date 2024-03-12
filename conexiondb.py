# This Python file us-es the following encoding: utf-8

# if __name__ == "__main__":
#     pass

import psycopg2 as pgsql

#Tablas: usuarios(id_usuario, usuario, password)
#conexiones(id, id_usuario, conexion)

class db:

    def __init__(self):
        self.dbname = "ejemplo"
        self.user = "admin"
        self.password = "admin"
        self.host = "localhost"
        self.conexion = None

    def conectar(self):
        try:
            conexion_nueva = pgsql.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host
            )
            self.conexion = conexion_nueva
        except Exception:
            print("Error al conectar la DB: %s", Exception.args)

    def coincide(self, usuario, contra):
        try:
            cursor = db.conexion.cursor()
            contra_s = str(contra)

            cursor.execute("SELECT * FROM usuarios WHERE usuario=%s AND password=%s", (usuario, contra_s))

            res = cursor.fetchone()

            if res:
                return True
            return False
        except Exception:
            return 'e'

    def obtener_id_usuario(self, usuario): # -> Chequear su funcionamiento
        try:
            cursor = db.conexion.cursor()

            cursor.execute("SELECT id_usuario FROM usuarios WHERE usuario=%s", (usuario,))

            res = cursor.fetchone()

            if res:
                return res
            return False
        except Exception as e:
            print("Error:", str(e))
            print("Tipo de error:", type(e))
            return 'e1'

    def obtener_datos(self, usuario): # -> Chequear su funcionamiento
        try:
            cursor = db.conexion.cursor()

            cursor.execute("SELECT conexion FROM conexiones WHERE id_usuario=%s", (self.obtener_id_usuario(usuario),))

            res = cursor.fetchall()

            return res
        except Exception:
            return 'e'

    def actualizar_datos(self, lista, usuario): # No funciona bien. REVISAR
        cursor = db.conexion.cursor()
        ultimo_id = db.obtener_ultimo_id()[0]
        i = 1
        for item in lista:
            cursor.execute("INSERT INTO conexiones (id, id_usuario, conexion) VALUES (%s, %s, %s)",
            (ultimo_id+i, self.obtener_id_usuario(usuario.nombre), item))
            i += 1

    def obtener_ultimo_id(self):
        cursor = db.conexion.cursor()
        cursor.execute("SELECT id FROM conexiones ORDER BY id DESC LIMIT 1")
        return cursor.fetchone()

    def guardar_datos(usuario):
        pass

"""
bd = db("ejemplo","admin","admin")
bd.conectar()
print(bd.coincide("Pato", 1234))
"""

db = db()
db.conectar() # Cuando importo la conexion en otros archivos, solamente importo la variable 'db'. De esa manera
                #, uso una sola conexion para todo el proyecto
