# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget, QDialog)
import time
import conexiondb as db
from ui_home import Ui_Dialog

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(742, 645)
        self.formLayoutWidget = QWidget(Widget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(190, 400, 321, 71))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.BotonEnviar1 = QPushButton(self.formLayoutWidget)
        self.BotonEnviar1.setObjectName(u"BotonEnviar1")
        self.BotonEnviar1.setEnabled(True)
        self.BotonEnviar1.setCursor(QCursor(Qt.PointingHandCursor))
        self.BotonEnviar1.setCheckable(False)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.BotonEnviar1)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 330, 101, 18))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 260, 101, 18))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"")
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 90, 521, 121))
        font = QFont()
        font.setFamilies([u"DejaVu Serif"])
        font.setPointSize(30)
        font.setBold(True)
        self.label_3.setFont(font)
        self.text_pass = QLineEdit(Widget)
        self.text_pass.setObjectName(u"text_pass")
        self.text_pass.setGeometry(QRect(190, 350, 321, 31))
        self.text_pass.setEchoMode(QLineEdit.Password)
        self.label_mensaje = QLabel(Widget)
        self.label_mensaje.setObjectName(u"label_mensaje")
        self.label_mensaje.setGeometry(QRect(190, 220, 511, 18))
        self.text_usuario = QLineEdit(Widget)
        self.text_usuario.setObjectName(u"text_usuario")
        self.text_usuario.setGeometry(QRect(190, 280, 321, 31))

        self.retranslateUi(Widget)
        self.BotonEnviar1.clicked.connect(lambda: inicio_sesion(self, Widget))

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"GPU Remote Manager", None))
        self.BotonEnviar1.setText(QCoreApplication.translate("Widget", u"Enviar", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Contrase\u00f1a", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Usuario", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Remote PC Manager", None))
        self.label_mensaje.setText(QCoreApplication.translate("Widget", u"-", None))
    # retranslateUi

def inicio_sesion(ui_widget, widget):
    bbdd = db.db("ejemplo", "admin", "admin")
    bbdd.conectar()
    user = ui_widget.text_usuario.text()
    passw = ui_widget.text_pass.text()
    mod_mensaje(ui_widget, "Validando inicio de sesion...", "none")
    QApplication.processEvents()
    time.sleep(2)
    res = bbdd.coincide(user, passw)

    # Se evalua el valor de 'res' para iniciar sesion
    if isinstance(res, str): # Cuando res = 'e', significa que hubo error en la conexion con la DB.
        mod_mensaje(ui_widget, "No se pudo conectar con la DB", "red")
    if res:
        mod_mensaje(ui_widget, "Sesion iniciada", "green")
        widget.close()
        iniciar_home()
    else:
        mod_mensaje(ui_widget, "Error: Usuario o contraseña incorrectos", "red")

def mod_mensaje(widget, texto, color):
    widget.label_mensaje.setStyleSheet(f"color: {color};")
    widget.label_mensaje.setText(texto)

def iniciar_home():
    dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    dialog.show()
    dialog.exec_()
