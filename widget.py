# This Python file uses the following encoding: utf-8
import sys
sys.path.append('ui/')
sys.path.append('controllers/')
from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from form_controller import FormController

class widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.controller = FormController(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = widget()
    widget.show()
    sys.exit(app.exec())
