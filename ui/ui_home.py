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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 381, 281))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.l_ip_propia = QLabel(self.layoutWidget)
        self.l_ip_propia.setObjectName(u"l_ip_propia")

        self.gridLayout.addWidget(self.l_ip_propia, 0, 0, 1, 2)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.b_nueva_conexion = QPushButton(self.layoutWidget)
        self.b_nueva_conexion.setObjectName(u"b_nueva_conexion")

        self.gridLayout.addWidget(self.b_nueva_conexion, 2, 1, 1, 1)

        self.lista_conexiones = QListWidget(self.layoutWidget)
        self.lista_conexiones.setObjectName(u"lista_conexiones")

        self.gridLayout.addWidget(self.lista_conexiones, 4, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Home", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Conexiones:", None))
        self.l_ip_propia.setText(QCoreApplication.translate("Dialog", u"Tu IP: ", None))
        self.b_nueva_conexion.setText(QCoreApplication.translate("Dialog", u"Nueva", None))
    # retranslateUi

