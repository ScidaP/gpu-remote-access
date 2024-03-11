# This Python file uses the following encoding: utf-8
from requests import get
from dialog_conexion import dialog_conexion
from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtWidgets import QListWidgetItem
from conexiondb import db
import sys

class homeController:
    def __init__(self, Dialog):
        self.crear_conexiones(Dialog)
        Dialog.ui.l_ip_propia.setText("Tu IP: %s" % obtener_ip())
        self.agregar_conexiones_lista(Dialog)

    def agregar_conexiones_lista(self, Dialog):
        data = db.obtener_datos('Pato')
        for item in data:
            dato = item[0]
            lista_item = QListWidgetItem(dato)
            Dialog.ui.lista_conexiones.addItem(lista_item)


    def crear_conexiones(self, Dialog):
        Dialog.ui.b_nueva_conexion.clicked.connect(abrir_dialog_conexion)
        Dialog.closeEvent = self.cerrar_programa
        #self.listView.doubleClicked.connect(self.item_doble_clic)

    #def item_doble_clic(self, index):
        #item_selecc = self.listView.data(index)
        #print("Doble clic en: ", item_selecc)

    def cerrar_programa(self, event):
        sys.exit()

def obtener_ip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return ip

def abrir_dialog_conexion():
    dialog = dialog_conexion()
    dialog.exec_()
