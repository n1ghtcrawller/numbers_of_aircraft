from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from finder1 import Ui_find_cirid
from findValues import find_value



class FindValues(QtWidgets.QMainWindow):
    def __init__(self):
        super(FindValues, self).__init__()
        self.ui = Ui_find_cirid()
        self.ui.setupUi(self)
        self.init_UI()


    def init_UI(self):
        self.setWindowTitle('Поиск данных для расчёта строчных применимостей')
        self.setWindowIcon(QIcon('airplane_icon-120x120.png'))
        self.ui.cirID.setPlaceholderText('%Введите cirID%')
        self.ui.applic_vlalue.setPlaceholderText('%Результат - applic_value%')
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.finder)

    def finder(self):
        input_cirID = self.ui.cirID.text()
        output_applicValue = find_value(input_cirID)
        self.ui.applic_vlalue.setText(str(output_applicValue))

