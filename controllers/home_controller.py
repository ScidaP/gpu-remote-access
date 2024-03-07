# This Python file uses the following encoding: utf-8
from requests import get

class homeController:
    def __init__(self, Dialog):
        self.crear_conexiones(Dialog)
        Dialog.ui.l_ip_propia.setText("Tu IP: %s" % obtener_ip())

    def crear_conexiones(self, Dialog): # la dejo declarada y la defino luego
        pass

def obtener_ip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return ip
