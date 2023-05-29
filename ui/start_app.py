from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from new_web import Ui_input_values
from finder_logic import FindValues
from dialog_logic import UIDiaWindow
import calculator_numbers
import adder


class InputValues(QtWidgets.QMainWindow):
    def __init__(self):
        super(InputValues, self).__init__()
        self.ui = Ui_input_values()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowIcon(QIcon('airplane_icon-120x120.png'))
        self.ui.descript.setPlaceholderText('Описание')
        self.ui.pushButton.clicked.connect(self.write_numbers)
        self.ui.pushButton_2.clicked.connect(self.OpenOtherWindow)
        self.ui.pushButton_4.clicked.connect(self.calculate_numbers)
        self.ui.pushButton_3.clicked.connect(self.close)
    # def converter(self):
    #     cirID = self.ui.cirID.text()
    #     applic_value = self.ui.applic_vlalue.text()
    #     output_dict = f'{cirID}: {applic_value}'
    #     self.ui.result.setText(str(output_dict))

    def OpenOtherWindow(self):
        global find_cirid
        find_cirid = QtWidgets.QDialog()
        self.app = FindValues()
        self.app.show()

    def OpenDialog(self):
        global dialog
        dialog = QtWidgets.QDialog()
        self.app = UIDiaWindow()
        self.app.show()

    def write_numbers(self):
        input_cirID = self.ui.cirID.text()
        input_evaluate = self.ui.applic_vlalue.text()
        input_resolve = self.ui.applic_vlalue_2.text()
        adder.add_object(input_cirID, input_evaluate, input_resolve)

    def calculate_numbers(self):
        calculator_numbers.getNumbersByValue()


