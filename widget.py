# This Python file uses the following encoding: utf-8
import sys
import conexiondb as db
from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

def inicio_sesion(widget):
    bbdd = db.db("ejemplo", "admin", "admin")
    bbdd.conectar()
    user = widget.ui.text_usuario.toPlainText()
    passw = widget.ui.text_pass.text()
    if bbdd.coincide(user, passw):
        widget.ui.label_mensaje.setText("Iniciando sesion...")
    widget.ui.label_mensaje.setStyleSheet("color: red;")
    widget.ui.label_mensaje.setText("Error: Usuario o contraseña incorrectos")


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.BotonEnviar1.clicked.connect(lambda: inicio_sesion(self))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
