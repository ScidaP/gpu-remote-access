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
    QPushButton, QSizePolicy, QTextEdit, QWidget)

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
        self.text_usuario = QTextEdit(Widget)
        self.text_usuario.setObjectName(u"text_usuario")
        self.text_usuario.setGeometry(QRect(190, 280, 321, 31))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 140, 521, 121))
        font = QFont()
        font.setFamilies([u"DejaVu Serif"])
        font.setPointSize(30)
        font.setBold(True)
        self.label_3.setFont(font)
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 350, 321, 31))
        self.lineEdit.setEchoMode(QLineEdit.Password)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"GPU Remote Manager", None))
        self.BotonEnviar1.setText(QCoreApplication.translate("Widget", u"Enviar", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Contrase\u00f1a", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Usuario", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Remote PC Manager", None))
    # retranslateUi

