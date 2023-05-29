import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from dialog2 import Ui_Form
import adder

class UIDiaWindow(QtWidgets.QWidget):
    def __init__(self):
        super(UIDiaWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle("Запись диапазона")
        self.ui.pushButton.clicked.connect(self.joinJSON)
        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.close)


    def joinJSON(self):
        pass



