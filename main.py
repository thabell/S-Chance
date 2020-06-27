import sys

import rule_card_form
from PyQt5 import QtCore, QtGui, QtWidgets
import structure


class RuleCardForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = rule_card_form.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.save_n_next_but.clicked.connect(self.save_n_next)
        self.ui.save_n_close_but.clicked.connect(self.save_n_close)
        self.ui.close_but.clicked.connect(self.close_ev)

    def save_n_next(self):
        state = self.ui.open_radio.isChecked()
        # print(state)
        description = self.ui.textEdit.toPlainText()
        self.ui.textEdit.setText("")
        # print(description)
        new_card = structure.Card(bool(state), str(description))
        print(new_card)

    def save_n_close(self):
        state = self.ui.open_radio.isChecked()
        # print(state)
        description = self.ui.textEdit.toPlainText()
        # print(description)
        new_card = structure.Card(bool(state), str(description))
        print(new_card)
        self.close()

    def close_ev(self):
        self.close()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    rule_card_window = RuleCardForm()
    rule_card_window.show()
    sys.exit(app.exec_())
