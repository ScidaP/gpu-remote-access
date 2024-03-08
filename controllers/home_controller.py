# This Python file uses the following encoding: utf-8
from requests import get
from dialog_conexion import dialog_conexion
from PySide6.QtCore import Qt

class homeController:
    def __init__(self, Dialog):
        self.crear_conexiones(Dialog)
        Dialog.ui.l_ip_propia.setText("Tu IP: %s" % obtener_ip())

    def crear_conexiones(self, Dialog): # la dejo declarada y la defino luego
        Dialog.ui.b_nueva_conexion.clicked.connect(abrir_dialog_conexion)

def obtener_ip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return ip

def abrir_dialog_conexion():
    dialog = dialog_conexion()
    dialog.exec_()
