# Form implementation generated from reading ui file 'finder.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_find_cirid(object):
    def setupUi(self, find_cirid):
        find_cirid.setObjectName("find_cirid")
        find_cirid.resize(531, 612)
        find_cirid.setStyleSheet("background-color: #00BFFF")
        self.cirID = QtWidgets.QLineEdit(parent=find_cirid)
        self.cirID.setGeometry(QtCore.QRect(80, 180, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Apple Symbols")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cirID.setFont(font)
        self.cirID.setStyleSheet("background-color: #00BFFF;\n"
"color: white;\n"
"font: 30pt \"Apple Symbols\";\n"
"border: 2px solid white;\n"
"border-radius: 30;")
        self.cirID.setFrame(False)
        self.cirID.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cirID.setObjectName("cirID")
        self.label = QtWidgets.QLabel(parent=find_cirid)
        self.label.setGeometry(QtCore.QRect(80, 30, 381, 131))
        font = QtGui.QFont()
        font.setFamily("Apple Symbols")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("text-align: center;\n"
"color: white;\n"
"border-color: white;\n"
"border-width: 2px;\n"
"font: 75 30pt \"Apple Symbols\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=find_cirid)
        self.pushButton.setGeometry(QtCore.QRect(80, 270, 381, 61))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: #00BFFF;\n"
"    background-color: white;\n"
"    border: 2px solid rgb(59, 131, 189);\n"
"    border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(200, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.applic_vlalue = QtWidgets.QLineEdit(parent=find_cirid)
        self.applic_vlalue.setGeometry(QtCore.QRect(80, 370, 380, 61))
        font = QtGui.QFont()
        font.setFamily("Apple Symbols")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.applic_vlalue.setFont(font)
        self.applic_vlalue.setStyleSheet("background-color: #00BFFF;\n"
"color: white;\n"
"font: 20pt \"Apple Symbols\";\n"
"border: 2px solid white;\n"
"border-radius: 30;")
        self.applic_vlalue.setFrame(False)
        self.applic_vlalue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.applic_vlalue.setObjectName("applic_vlalue")
        self.pushButton_2 = QtWidgets.QPushButton(parent=find_cirid)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 470, 381, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: #00BFFF;\n"
"    background-color: white;\n"
"    border: 2px solid rgb(59, 131, 189);\n"
"    border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgb(200, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(find_cirid)
        QtCore.QMetaObject.connectSlotsByName(find_cirid)

    def retranslateUi(self, find_cirid):
        _translate = QtCore.QCoreApplication.translate
        find_cirid.setWindowTitle(_translate("find_cirid", "Dialog"))
        self.label.setText(_translate("find_cirid", "<html><head/><body><p align=\"center\">Поиск диапазонов </p><p align=\"center\">по ключу <span style=\" font-size:36pt; font-weight:600;\">cir_ID</span></p></body></html>"))
        self.pushButton.setText(_translate("find_cirid", "ПОИСК"))
        self.pushButton_2.setText(_translate("find_cirid", "ЗАКРЫТЬ"))

