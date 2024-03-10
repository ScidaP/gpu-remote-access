# This Python file uses the following encoding: utf-8
from requests import get
from dialog_conexion import dialog_conexion
from PySide6.QtCore import Qt, QStringListModel
from conexiondb import db

class homeController:
    def __init__(self, Dialog):
        self.crear_conexiones(Dialog)
        Dialog.ui.l_ip_propia.setText("Tu IP: %s" % obtener_ip())
        model = obtener_model()
        Dialog.ui.listado_conexiones.setModel(model)

    def crear_conexiones(self, Dialog):
        Dialog.ui.b_nueva_conexion.clicked.connect(abrir_dialog_conexion)

def obtener_ip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return ip

def abrir_dialog_conexion():
    dialog = dialog_conexion()
    dialog.exec_()

def obtener_model():
    # Busco la info cargada al usuario correspondiente en la db y se guarda en la vble 'data'
    # Formato correcto de los datos: data = ['ejemplo', 'uno', '188.90.23.222', '240.12.12.231']
    db.obtener_datos('pato')
    data = ['ejemplo', 'uno', '188.90.23.222', '240.12.12.231']
    model = QStringListModel()
    model.setStringList(data)
    return model
