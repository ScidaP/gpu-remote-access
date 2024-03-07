# This Python file uses the following encoding: utf-8
import sys
sys.path.append('ui/')
sys.path.append('controllers/')
from PySide6.QtWidgets import QApplication, QWidget, QDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_home import Ui_Dialog
from home_controller import homeController

class dialog_home(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.controller = homeController(self)

