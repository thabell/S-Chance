# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choice_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.new_choice = QtWidgets.QLineEdit(self.centralwidget)
        self.new_choice.setGeometry(QtCore.QRect(180, 60, 381, 21))
        self.new_choice.setObjectName("new_choice")
        self.new_choice_label = QtWidgets.QLabel(self.centralwidget)
        self.new_choice_label.setGeometry(QtCore.QRect(10, 60, 161, 20))
        self.new_choice_label.setObjectName("new_choice_label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 211, 21))
        self.label_2.setObjectName("label_2")
        self.save_n_close_but = QtWidgets.QPushButton(self.centralwidget)
        self.save_n_close_but.setGeometry(QtCore.QRect(240, 110, 221, 41))
        self.save_n_close_but.setObjectName("save_n_close_but")
        self.close_but = QtWidgets.QPushButton(self.centralwidget)
        self.close_but.setGeometry(QtCore.QRect(470, 110, 91, 41))
        self.close_but.setObjectName("close_but")
        self.save_n_next_but = QtWidgets.QPushButton(self.centralwidget)
        self.save_n_next_but.setGeometry(QtCore.QRect(10, 110, 221, 41))
        self.save_n_next_but.setObjectName("save_n_next_but")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавление варианта ответа"))
        self.new_choice_label.setText(_translate("MainWindow", "Текст варианта ответа"))
        self.label_2.setText(_translate("MainWindow", "Добавление варианта ответа"))
        self.save_n_close_but.setText(_translate("MainWindow", "Сохранить и закрыть"))
        self.close_but.setText(_translate("MainWindow", "Закрыть"))
        self.save_n_next_but.setText(_translate("MainWindow", "Сохранить и добавить следующую"))