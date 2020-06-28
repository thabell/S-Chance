import sys
import structure
import rule_card_form
import tip_card_form
import history_card_form
import add_card
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class CardForm(QtWidgets.QMainWindow):
    def __init__(self, form, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = form.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.save_n_next_but.clicked.connect(self.save_n_next)
        self.ui.save_n_close_but.clicked.connect(self.save_n_close)
        self.ui.close_but.clicked.connect(self.close_ev)

    # abstractmethod
    def save_n_next(self):
        pass

    # abstractmethod
    def save_n_close(self):
        pass

    def close_ev(self):
        self.close()


class RuleCardForm(CardForm):
    def __init__(self, parent=None):
        super().__init__(rule_card_form, parent)

    def save_n_next(self):
        state = self.ui.open_radio.isChecked()
        description = self.ui.textEdit.toPlainText()
        self.ui.textEdit.setText("")
        new_card = structure.Card(bool(state), str(description))
        structure.write_to_db_to_cards(new_card)

    def save_n_close(self):
        state = self.ui.open_radio.isChecked()
        description = self.ui.textEdit.toPlainText()
        new_card = structure.Card(bool(state), str(description))
        structure.write_to_db_to_cards(new_card)
        self.close()

class TipCardForm(CardForm):
    def __init__(self, parent=None):
        super().__init__(tip_card_form, parent)

    def save_n_next(self):
        state = self.ui.open_radio.isChecked()
        description = self.ui.textEdit.toPlainText()
        name = self.ui.card_name.toPlainText()
        self.ui.textEdit.setText("")
        self.ui.card_name.setText("")
        new_card = structure.Card_tip(bool(state), str(description), str(name))
        print(new_card)
        structure.write_to_db_to_cards_tip(new_card)

    def save_n_close(self):
        state = self.ui.open_radio.isChecked()
        description = self.ui.textEdit.toPlainText()
        name = self.ui.card_name.text()
        new_card = structure.Card_tip(bool(state), str(description), str(name))
        structure.write_to_db_to_cards_tip(new_card)
        self.close()

class HistoryCardForm(CardForm):
    def __init__(self, parent=None):
        super().__init__(history_card_form, parent)
        self.ui.add_new_var_but.clicked.connect(self.add_new_var)

    def add_new_var(self):
        # print(self.ui.card_choises.children())
        ix = len(self.ui.card_choises.children())
        new_label = QtWidgets.QLabel(self.ui.card_choises)
        new_label.setGeometry(QtCore.QRect(0, 70 + (20 * (ix - 3)), 111, 16))
        new_label.setObjectName("label_" + str(ix))
        new_label.show()
        new_label.setText(QtCore.QCoreApplication.translate("MainWindow", "Еще вариант ответа"))
        new_card_choices_item = QtWidgets.QLineEdit(self.ui.card_choises)
        new_card_choices_item.setGeometry(QtCore.QRect(120, 70 + (20 * (ix - 3)), 431, 21))
        new_card_choices_item.setObjectName("card_choices_item_" + str(ix))
        new_card_choices_item.show()
        old_coords = self.ui.card_choises.geometry().getRect()
        self.ui.card_choises.setGeometry(QtCore.QRect(old_coords[0], old_coords[1], old_coords[2], old_coords[3] + 40))
        old_coords2 = self.ui.add_new_var_but.geometry().getRect()
        self.ui.add_new_var_but.setGeometry(QtCore.QRect(old_coords2[0], old_coords2[1] + 40, old_coords2[2], old_coords2[3]))
        old_coords3 = self.ui.submit_buttons.geometry().getRect()
        self.ui.submit_buttons.setGeometry(QtCore.QRect(old_coords3[0], old_coords3[1] + 40, old_coords3[2], old_coords3[3]))
        old_coords4 = self.geometry().getRect()
        self.setGeometry(QtCore.QRect(old_coords4[0], old_coords4[1], old_coords4[2], old_coords4[3] + 40))

    def save_n_next(self):
        state = self.ui.open_radio.isChecked()
        description = self.ui.textEdit.toPlainText()
        prescription = self.ui.card_prescription.text()
        scene = self.ui.card_scene.text()
        valid_date = self.ui.card_valid_date.text()
        choices = self.ui.card_choises.children()
        choices_ = list()
        for choice in choices:
            if isinstance(choice, QtWidgets.QLineEdit):
                choices_.append(str(choice.text()))
                choice.setText("")
        self.ui.textEdit.setText("")
        self.ui.card_prescription.setText("")
        self.ui.card_scene.setText("")
        self.ui.card_valid_date.setText("")
        new_card = structure.History_card(
            bool(state), str(description), str(prescription), str(scene), str(valid_date), choices_)
        print(new_card)
        structure.write_to_db_to_history_cards(new_card)

    def save_n_close(self):
        state = self.ui.open_radio.isChecked()
        description = self.ui.textEdit.toPlainText()
        prescription = self.ui.card_prescription.text()
        scene = self.ui.card_scene.text()
        valid_date = self.ui.card_valid_date.text()
        choices = self.ui.card_choises.children()
        choices_ = list()
        for choice in choices:
            if isinstance(choice, QtWidgets.QLineEdit):
                choices_.append(str(choice.text()))
        new_card = structure.History_card(
            bool(state), str(description), str(prescription), str(scene), str(valid_date), choices_)
        print(new_card)
        structure.write_to_db_to_history_cards(new_card)
        self.close()

class AddCardForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = add_card.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.new_rule_card_but.clicked.connect(self.new_rule_card_init)
        self.ui.new_tip_card_but.clicked.connect(self.new_tip_card_init)
        self.ui.new_history_card_but.clicked.connect(self.new_history_card_init)
        self.ui.close_but.clicked.connect(self.close_ev)

    def new_rule_card_init(self):
        rule_card_window = RuleCardForm(self)
        rule_card_window.show()

    def new_tip_card_init(self):
        tip_card_window = TipCardForm(self)
        tip_card_window.show()

    def new_history_card_init(self):
        history_card_window = HistoryCardForm(self)
        history_card_window.show()

    def close_ev(self):
        self.close()


if __name__=="__main__":
    # structure.create_db_to_history_cards()
    app = QtWidgets.QApplication(sys.argv)
    add_card_window = AddCardForm()
    add_card_window.show()
    sys.exit(app.exec_())
