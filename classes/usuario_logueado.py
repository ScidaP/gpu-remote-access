# This Python file uses the following encoding: utf-8
from datetime import datetime
import pytz

argentina_timezone = pytz.timezone('America/Argentina/Buenos_Aires')

class usuario_logueado:
    def __init__(self, nombre=None):
        self.nombre = nombre;
        self.hora_logueo = datetime.now(argentina_timezone)

usuario = usuario_logueado()
