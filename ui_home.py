# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QListView, QPushButton, QSizePolicy, QWidget)
from requests import get

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.l_ip_propia = QLabel(Dialog)
        self.l_ip_propia.setObjectName(u"l_ip_propia")
        self.l_ip_propia.setGeometry(QRect(10, 10, 221, 18))
        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 30, 221, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 111, 18))
        font = QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.b_nueva_conexion = QPushButton(Dialog)
        self.b_nueva_conexion.setObjectName(u"b_nueva_conexion")
        self.b_nueva_conexion.setGeometry(QRect(140, 50, 87, 26))
        self.listado_conexiones = QListView(Dialog)
        self.listado_conexiones.setObjectName(u"listado_conexiones")
        self.listado_conexiones.setGeometry(QRect(10, 90, 371, 192))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.l_ip_propia.setText(QCoreApplication.translate("Dialog", u"Tu IP: %s" % obtener_ip(), None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Conexiones:", None))
        self.b_nueva_conexion.setText(QCoreApplication.translate("Dialog", u"Nueva", None))
    # retranslateUi

def obtener_ip():
    ip = get('https://api.ipify.org').content.decode('utf8')
    return ip
