# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QDialog
import time
import conexiondb as db
from ui_home import Ui_Dialog

class FormController:
    def __init__(self, Widget):
        self.crear_conexiones(Widget)

    def crear_conexiones(self, Widget):
        Widget.ui.BotonEnviar1.clicked.connect(lambda: inicio_sesion(Widget))

def inicio_sesion(widget):
    bbdd = db.db("ejemplo", "admin", "admin")
    bbdd.conectar()
    user = widget.ui.text_usuario.text()
    passw = widget.ui.text_pass.text()
    mod_mensaje(widget, "Validando inicio de sesion...", "none")
    QApplication.processEvents()
    time.sleep(2)
    res = bbdd.coincide(user, passw)

    # Se evalua el valor de 'res' para iniciar sesion
    if isinstance(res, str): # Cuando res = 'e', significa que hubo error en la conexion con la DB.
        mod_mensaje(widget, "No se pudo conectar con la DB", "red")
    if res:
        mod_mensaje(widget, "Sesion iniciada", "green")
        widget.close()
        iniciar_home()
    else:
        mod_mensaje(widget, "Error: Usuario o contraseña incorrectos", "red")

def mod_mensaje(widget, texto, color):
    widget.ui.label_mensaje.setStyleSheet(f"color: {color};")
    widget.ui.label_mensaje.setText(texto)

def iniciar_home():
    dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    dialog.exec_()
