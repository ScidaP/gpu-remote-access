# This Python file uses the following encoding: utf-8
from requests import get
from dialog_conexion import dialog_conexion
from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtWidgets import QListWidgetItem, QInputDialog, QMessageBox, QLineEdit
from conexiondb import db
import sys
sys.path.append("/home/patricio/pythonUIproj/pythUIProj/classes")
from usuario_logueado import usuario

class homeController: # MANEJAR QListWidget : https://www.youtube.com/watch?v=InM-9LLhdnI&ab_channel=TurtleCode
    def __init__(self, Dialog):
        self.crear_conexiones(Dialog)
        Dialog.ui.l_ip_propia.setText("Tu IP: %s" % obtener_ip())
        self.cargar_conexiones_lista(Dialog)

    def cargar_conexiones_lista(self, Dialog): # Carga los items que hay en la DB
        data = db.obtener_datos('Pato')
        for item in data:
            dato = item[0]
            lista_item = QListWidgetItem(dato)
            Dialog.ui.lista_conexiones.addItem(lista_item)

    def crear_conexiones(self, Dialog):
        Dialog.closeEvent = self.cerrar_programa
        Dialog.ui.b_nueva_conexion.clicked.connect(lambda: agregar_item_lista(Dialog))
        Dialog.ui.b_borrar_conexion.clicked.connect(lambda: eliminar_item_lista(Dialog))
        Dialog.ui.b_editar_conexion.clicked.connect(lambda: editar_item_lista(Dialog))
        Dialog.ui.b_actualizar_db.clicked.connect(lambda: actualizar_datos_db(Dialog))

    def cerrar_programa(self, event):
        sys.exit()

def actualizar_datos_db(Dialog): # Falta desarrollar
    lista_items = list()

    for i in range(Dialog.ui.lista_conexiones.count()):
        lista_items.append(Dialog.ui.lista_conexiones.item(i).text())
    #QMessageBox.information(Dialog, "Info", "DB actualizada con éxito")
    # Filtro las conexiones que ya existían y las quito de la lista

    lista_filtrada = filtrar_conexiones_existentes(Dialog, lista_items)

    # Ahora actualizo las conexiones en la DB
    db.actualizar_datos(lista_filtrada, usuario)

def filtrar_conexiones_existentes(Dialog, lista_items):
    conexiones_db = db.obtener_datos('Pato')
    for item in conexiones_db:
        dato = item[0]
        if (dato in lista_items):
            lista_items.remove(dato)
    return lista_items

def agregar_item_lista(Dialog):
    indice_actual = Dialog.ui.lista_conexiones.currentRow()
    texto, ok = QInputDialog.getText(Dialog, "Nueva Conexión", "Conexion")
    if ok and texto is not None:
        Dialog.ui.lista_conexiones.insertItem(indice_actual, texto)

def eliminar_item_lista(Dialog):
    indice_actual = Dialog.ui.lista_conexiones.currentRow()
    item = Dialog.ui.lista_conexiones.item(indice_actual)
    if item is None:
        return

    pregunta = QMessageBox.question(Dialog, "Eliminar Conexion", "¿Quieres eliminar la conexión: " + item.text() + "?",
    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

    if pregunta == QMessageBox.StandardButton.Yes:
        item = Dialog.ui.lista_conexiones.takeItem(indice_actual)
        del item

def editar_item_lista(Dialog):
    indice_actual = Dialog.ui.lista_conexiones.currentRow()
    item = Dialog.ui.lista_conexiones.item(indice_actual)
    if item is not None:
        text, ok = QInputDialog.getText(Dialog, "Cambiar IP Conexion", "Conexion", QLineEdit.Normal, item.text())
        if text and ok is not None:
            item.setText(text)


def obtener_ip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return ip
