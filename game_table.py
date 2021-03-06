# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_table.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("overflow: auto;")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 1371, 921))
        self.label_6.setStyleSheet("<resource type=\"other\" file=\":/fonts/static/Lato-Semibold.ttf\"/>\n"
"")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/img/static/back.jpeg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.greeting_box = QtWidgets.QWidget(self.centralwidget)
        self.greeting_box.setEnabled(True)
        self.greeting_box.setGeometry(QtCore.QRect(480, 80, 401, 511))
        self.greeting_box.setStyleSheet("")
        self.greeting_box.setObjectName("greeting_box")
        self.label_4 = QtWidgets.QLabel(self.greeting_box)
        self.label_4.setGeometry(QtCore.QRect(110, 0, 191, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/img/static/01.jpg"))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.greeting_box)
        self.label_5.setGeometry(QtCore.QRect(10, 280, 381, 151))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 11pt \"Lato Semibold\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.spread_the_cards_but = QtWidgets.QPushButton(self.greeting_box)
        self.spread_the_cards_but.setGeometry(QtCore.QRect(110, 450, 181, 51))
        self.spread_the_cards_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spread_the_cards_but.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 3px;\n"
"font: 63 11pt \"Lato Semibold\";")
        self.spread_the_cards_but.setObjectName("spread_the_cards_but")
        self.action_card_box = QtWidgets.QWidget(self.centralwidget)
        self.action_card_box.setEnabled(True)
        self.action_card_box.setGeometry(QtCore.QRect(510, 10, 350, 621))
        self.action_card_box.setStyleSheet("")
        self.action_card_box.setObjectName("action_card_box")
        self.flip_the_card_but = QtWidgets.QPushButton(self.action_card_box)
        self.flip_the_card_but.setGeometry(QtCore.QRect(80, 560, 181, 51))
        self.flip_the_card_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.flip_the_card_but.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 3px;\n"
"font: 63 11pt \"Lato Semibold\";")
        self.flip_the_card_but.setObjectName("flip_the_card_but")
        self.action_card_name = QtWidgets.QLabel(self.action_card_box)
        self.action_card_name.setGeometry(QtCore.QRect(90, 10, 161, 31))
        self.action_card_name.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 11pt \"Lato Semibold\";")
        self.action_card_name.setAlignment(QtCore.Qt.AlignCenter)
        self.action_card_name.setWordWrap(True)
        self.action_card_name.setObjectName("action_card_name")
        self.card_back = QtWidgets.QWidget(self.action_card_box)
        self.card_back.setGeometry(QtCore.QRect(0, 50, 350, 450))
        self.card_back.setObjectName("card_back")
        self.card_front = QtWidgets.QWidget(self.action_card_box)
        self.card_front.setGeometry(QtCore.QRect(0, 50, 350, 500))
        self.card_front.setObjectName("card_front")
        self.card_back.raise_()
        self.card_front.raise_()
        self.flip_the_card_but.raise_()
        self.action_card_name.raise_()
        self.rule_cards_box = QtWidgets.QWidget(self.centralwidget)
        self.rule_cards_box.setGeometry(QtCore.QRect(17, 20, 181, 251))
        self.rule_cards_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.rule_cards_box.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 11pt \"Lato Semibold\";")
        self.rule_cards_box.setObjectName("rule_cards_box")
        self.label_17 = QtWidgets.QLabel(self.rule_cards_box)
        self.label_17.setGeometry(QtCore.QRect(30, 0, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.point_cards_box = QtWidgets.QWidget(self.centralwidget)
        self.point_cards_box.setGeometry(QtCore.QRect(940, 30, 140, 121))
        self.point_cards_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.point_cards_box.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 11pt \"Lato Semibold\";")
        self.point_cards_box.setObjectName("point_cards_box")
        self.label_18 = QtWidgets.QLabel(self.point_cards_box)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.tip_cards_box = QtWidgets.QWidget(self.centralwidget)
        self.tip_cards_box.setGeometry(QtCore.QRect(900, 500, 421, 191))
        self.tip_cards_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tip_cards_box.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 11pt \"Lato Semibold\";")
        self.tip_cards_box.setObjectName("tip_cards_box")
        self.widget_14 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_14.setGeometry(QtCore.QRect(20, 40, 71, 41))
        self.widget_14.setObjectName("widget_14")
        self.widget_15 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_15.setGeometry(QtCore.QRect(100, 40, 71, 41))
        self.widget_15.setObjectName("widget_15")
        self.widget_16 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_16.setGeometry(QtCore.QRect(180, 40, 71, 41))
        self.widget_16.setObjectName("widget_16")
        self.widget_17 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_17.setGeometry(QtCore.QRect(260, 40, 71, 41))
        self.widget_17.setObjectName("widget_17")
        self.widget_18 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_18.setGeometry(QtCore.QRect(340, 40, 71, 41))
        self.widget_18.setObjectName("widget_18")
        self.widget_19 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_19.setGeometry(QtCore.QRect(20, 90, 71, 41))
        self.widget_19.setObjectName("widget_19")
        self.widget_20 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_20.setGeometry(QtCore.QRect(100, 90, 71, 41))
        self.widget_20.setObjectName("widget_20")
        self.widget_21 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_21.setGeometry(QtCore.QRect(180, 90, 71, 41))
        self.widget_21.setObjectName("widget_21")
        self.widget_22 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_22.setGeometry(QtCore.QRect(260, 90, 71, 41))
        self.widget_22.setObjectName("widget_22")
        self.widget_23 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_23.setGeometry(QtCore.QRect(340, 90, 71, 41))
        self.widget_23.setObjectName("widget_23")
        self.widget_24 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_24.setGeometry(QtCore.QRect(60, 140, 71, 41))
        self.widget_24.setObjectName("widget_24")
        self.widget_26 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_26.setGeometry(QtCore.QRect(140, 140, 71, 41))
        self.widget_26.setObjectName("widget_26")
        self.widget_25 = QtWidgets.QWidget(self.tip_cards_box)
        self.widget_25.setGeometry(QtCore.QRect(220, 140, 71, 41))
        self.widget_25.setObjectName("widget_25")
        self.tip_cards_box_title = QtWidgets.QLabel(self.tip_cards_box)
        self.tip_cards_box_title.setGeometry(QtCore.QRect(20, 0, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.tip_cards_box_title.setFont(font)
        self.tip_cards_box_title.setStyleSheet("")
        self.tip_cards_box_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tip_cards_box_title.setObjectName("tip_cards_box_title")
        self.res_wrapper = QtWidgets.QWidget(self.centralwidget)
        self.res_wrapper.setGeometry(QtCore.QRect(1190, 20, 148, 485))
        self.res_wrapper.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Lato Semibold\";")
        self.res_wrapper.setObjectName("res_wrapper")
        self.label_20 = QtWidgets.QLabel(self.res_wrapper)
        self.label_20.setGeometry(QtCore.QRect(0, 0, 148, 30))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.results_table = QtWidgets.QLabel(self.res_wrapper)
        self.results_table.setGeometry(QtCore.QRect(0, 30, 148, 455))
        self.results_table.setStyleSheet("font: 9pt;")
        self.results_table.setObjectName("results_table")
        self.solution_cards_box = QtWidgets.QWidget(self.centralwidget)
        self.solution_cards_box.setGeometry(QtCore.QRect(280, 20, 181, 251))
        self.solution_cards_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.solution_cards_box.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 11pt \"Lato Semibold\";")
        self.solution_cards_box.setObjectName("solution_cards_box")
        self.label_19 = QtWidgets.QLabel(self.solution_cards_box)
        self.label_19.setGeometry(QtCore.QRect(30, 0, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.thanks = QtWidgets.QLabel(self.centralwidget)
        self.thanks.setGeometry(QtCore.QRect(920, 200, 191, 61))
        self.thanks.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 20pt \"Capitol deco\";")
        self.thanks.setAlignment(QtCore.Qt.AlignCenter)
        self.thanks.setWordWrap(True)
        self.thanks.setObjectName("thanks")
        self.history_cards_box = QtWidgets.QWidget(self.centralwidget)
        self.history_cards_box.setGeometry(QtCore.QRect(20, 300, 421, 401))
        self.history_cards_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.history_cards_box.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 11pt \"Lato Semibold\";")
        self.history_cards_box.setObjectName("history_cards_box")
        self.widget_27 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_27.setGeometry(QtCore.QRect(20, 40, 71, 110))
        self.widget_27.setObjectName("widget_27")
        self.widget_28 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_28.setGeometry(QtCore.QRect(100, 40, 71, 110))
        self.widget_28.setObjectName("widget_28")
        self.widget_29 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_29.setGeometry(QtCore.QRect(180, 40, 71, 110))
        self.widget_29.setObjectName("widget_29")
        self.widget_30 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_30.setGeometry(QtCore.QRect(260, 40, 71, 110))
        self.widget_30.setObjectName("widget_30")
        self.widget_31 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_31.setGeometry(QtCore.QRect(340, 40, 71, 110))
        self.widget_31.setObjectName("widget_31")
        self.widget_32 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_32.setGeometry(QtCore.QRect(20, 160, 71, 110))
        self.widget_32.setObjectName("widget_32")
        self.widget_33 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_33.setGeometry(QtCore.QRect(100, 160, 71, 110))
        self.widget_33.setObjectName("widget_33")
        self.widget_34 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_34.setGeometry(QtCore.QRect(180, 160, 71, 110))
        self.widget_34.setObjectName("widget_34")
        self.widget_35 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_35.setGeometry(QtCore.QRect(260, 160, 71, 110))
        self.widget_35.setObjectName("widget_35")
        self.widget_36 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_36.setGeometry(QtCore.QRect(340, 160, 71, 110))
        self.widget_36.setObjectName("widget_36")
        self.widget_37 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_37.setGeometry(QtCore.QRect(60, 280, 71, 110))
        self.widget_37.setObjectName("widget_37")
        self.widget_39 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_39.setGeometry(QtCore.QRect(140, 280, 71, 110))
        self.widget_39.setObjectName("widget_39")
        self.widget_40 = QtWidgets.QWidget(self.history_cards_box)
        self.widget_40.setGeometry(QtCore.QRect(220, 280, 71, 110))
        self.widget_40.setObjectName("widget_40")
        self.history_cards_box_title = QtWidgets.QLabel(self.history_cards_box)
        self.history_cards_box_title.setGeometry(QtCore.QRect(20, 0, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.history_cards_box_title.setFont(font)
        self.history_cards_box_title.setStyleSheet("")
        self.history_cards_box_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.history_cards_box_title.setObjectName("history_cards_box_title")
        self.imitation_step = QtWidgets.QPushButton(self.centralwidget)
        self.imitation_step.setGeometry(QtCore.QRect(490, 640, 181, 51))
        self.imitation_step.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.imitation_step.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 3px;\n"
"font: 63 11pt \"Lato Semibold\";")
        self.imitation_step.setObjectName("imitation_step")
        self.whole_imitation = QtWidgets.QPushButton(self.centralwidget)
        self.whole_imitation.setGeometry(QtCore.QRect(690, 640, 181, 51))
        self.whole_imitation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.whole_imitation.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 3px;\n"
"font: 63 11pt \"Lato Semibold\";")
        self.whole_imitation.setObjectName("whole_imitation")
        self.imitation_log = QtWidgets.QLabel(self.centralwidget)
        self.imitation_log.setGeometry(QtCore.QRect(880, 280, 291, 211))
        self.imitation_log.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"Consolas\";")
        self.imitation_log.setAlignment(QtCore.Qt.AlignCenter)
        self.imitation_log.setWordWrap(True)
        self.imitation_log.setObjectName("imitation_log")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.add_cards_but = QtWidgets.QAction(MainWindow)
        self.add_cards_but.setObjectName("add_cards_but")
        self.menu.addAction(self.add_cards_but)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "S-Chance"))
        self.label_5.setText(_translate("MainWindow", "Вашему вниманию представляется игра\n"
"\"Второй шанс. Смерть музыканта\".\n"
"Вам предстоит отправиться в Чикаго 20-х годов. Плюшевый мишка рядом с лужей крови... Должны ли поиски счастья закончиться смертью?\n"
"Вы - творцы судьбы. Собирая прошлое человека из осколков вы должны понять его судьбу и предотвратить смерть."))
        self.spread_the_cards_but.setText(_translate("MainWindow", "Разложить карты"))
        self.flip_the_card_but.setText(_translate("MainWindow", "Перевернуть карту"))
        self.action_card_name.setText(_translate("MainWindow", "Просмотр карты"))
        self.label_17.setText(_translate("MainWindow", "Карты Правил"))
        self.label_18.setText(_translate("MainWindow", "Карты Судьбы"))
        self.tip_cards_box_title.setText(_translate("MainWindow", "Карты Подсказки (осталось открыть 5)"))
        self.label_20.setText(_translate("MainWindow", "Ход игры"))
        self.results_table.setText(_translate("MainWindow", "results_table"))
        self.label_19.setText(_translate("MainWindow", "Карты Решения"))
        self.thanks.setText(_translate("MainWindow", "Благодарим\n"
"за игру!"))
        self.history_cards_box_title.setText(_translate("MainWindow", "Карты Истории (осталось открыть 10)"))
        self.imitation_step.setText(_translate("MainWindow", "Шаг имитации"))
        self.whole_imitation.setText(_translate("MainWindow", "Имитация всей игры"))
        self.imitation_log.setText(_translate("MainWindow", "imitation_log"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.add_cards_but.setText(_translate("MainWindow", "Добавить карты"))
import resources_rc
