# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rule_card_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 421, 16))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 80, 291, 71))
        self.groupBox.setObjectName("groupBox")
        self.open_radio = QtWidgets.QRadioButton(self.groupBox)
        self.open_radio.setGeometry(QtCore.QRect(20, 20, 141, 17))
        self.open_radio.setChecked(False)
        self.open_radio.setObjectName("open_radio")
        self.closed_radio = QtWidgets.QRadioButton(self.groupBox)
        self.closed_radio.setGeometry(QtCore.QRect(20, 40, 151, 17))
        self.closed_radio.setChecked(True)
        self.closed_radio.setObjectName("closed_radio")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 200, 551, 141))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 170, 131, 16))
        self.label_2.setObjectName("label_2")
        self.save_n_next_but = QtWidgets.QPushButton(self.centralwidget)
        self.save_n_next_but.setGeometry(QtCore.QRect(50, 350, 221, 41))
        self.save_n_next_but.setObjectName("save_n_next_but")
        self.save_n_close_but = QtWidgets.QPushButton(self.centralwidget)
        self.save_n_close_but.setGeometry(QtCore.QRect(280, 350, 221, 41))
        self.save_n_close_but.setObjectName("save_n_close_but")
        self.close_but = QtWidgets.QPushButton(self.centralwidget)
        self.close_but.setGeometry(QtCore.QRect(510, 350, 91, 41))
        self.close_but.setObjectName("close_but")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Создание новой Карты с описанием игры (Карты правил, Завершающие карты)"))
        self.groupBox.setTitle(_translate("MainWindow", "Открыта или закрыта (прочитана или не прочитана)"))
        self.open_radio.setText(_translate("MainWindow", "Открыта (прочитана)"))
        self.closed_radio.setText(_translate("MainWindow", "Закрыта (не прочитана)"))
        self.label_2.setText(_translate("MainWindow", "Надпись на самой карте"))
        self.save_n_next_but.setText(_translate("MainWindow", "Сохранить и добавить следующую"))
        self.save_n_close_but.setText(_translate("MainWindow", "Сохранить и закрыть"))
        self.close_but.setText(_translate("MainWindow", "Закрыть"))
