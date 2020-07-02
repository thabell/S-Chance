import sys
import structure
import rule_card_form
import tip_card_form
import history_card_form
import choice_form
import point_card_form
import add_card
import error_message
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class ErrorMessage(QtWidgets.QMainWindow):
    def __init__(self, mess="Подробностей нет", parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = error_message.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.details.setText(mess)

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
        number = self.ui.card_number.text()
        state = self.ui.open_radio.isChecked()
        description = self.ui.card_description.toPlainText()
        self.ui.card_description.setText("")
        self.ui.card_number.setText("")
        new_card = structure.Card(int(number), int(state), str(description))
        new_card.write_to_bd()

    def save_n_close(self):
        number = self.ui.card_number.text()
        state = self.ui.open_radio.isChecked()
        description = self.ui.card_description.toPlainText()
        new_card = structure.Card(int(number), int(state), str(description))
        new_card.write_to_bd()
        self.close()


class ChoiceForm(CardForm):
    def __init__(self, parent=None):
        super().__init__(choice_form, parent)
        self.ui.new_choice_label.setText("Текст варианта ответа № " + str(len(self.parent().card.get_choices()) + 1))

    def save_n_next(self):
        try:
            possible_answer = len(self.parent().card.get_choices()) + 1
            text = self.ui.new_choice.text()
            number_card_history = self.parent().card.get_number()
            new_choice = structure.Choices(possible_answer, text, number_card_history)
            print(new_choice)
            self.parent().card.get_choices().append(new_choice)
            print(self.parent().card.get_choices())
            self.parent().reload_curr_choices()
            self.ui.new_choice.setText("")
            self.ui.new_choice_label.setText("Текст варианта ответа № " + str(len(self.parent().card.get_choices()) + 1))
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в ChoiceForm", self).show()

    def save_n_close(self):
        try:
            possible_answer = len(self.parent().card.get_choices()) + 1
            text = self.ui.new_choice.text()
            number_card_history = self.parent().card.get_number()
            new_choice = structure.Choices(possible_answer, text, number_card_history)
            print(new_choice)
            self.parent().card.get_choices().append(new_choice)
            print(self.parent().card.get_choices())
            self.parent().reload_curr_choices()
            self.close()
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в ChoiceForm", self).show()
        # ix = len(self.ui.card_choises.children())
        # new_label = QtWidgets.QLabel(self.ui.card_choises)
        # new_label.setGeometry(QtCore.QRect(0, 70 + (20 * (ix - 3)), 111, 16))
        # new_label.setObjectName("label_" + str(ix))
        # new_label.show()
        # new_label.setText(QtCore.QCoreApplication.translate("MainWindow", "Еще вариант ответа"))
        # new_card_choices_item = QtWidgets.QLineEdit(self.ui.card_choises)
        # new_card_choices_item.setGeometry(QtCore.QRect(120, 70 + (20 * (ix - 3)), 431, 21))
        # new_card_choices_item.setObjectName("card_choices_item_" + str(ix))
        # new_card_choices_item.show()
        # old_coords = self.ui.card_choises.geometry().getRect()
        # self.ui.card_choises.setGeometry(QtCore.QRect(old_coords[0],old_coords[1], old_coords[2], old_coords[3] + 40))


class TipCardForm(CardForm):
    def __init__(self, parent=None):
        super().__init__(tip_card_form, parent)
        self.ui.save_n_next_but.hide()

    def save_n_close(self):
        try:
            number = self.parent().card.get_number()
            state = self.ui.open_radio.isChecked()
            description = self.ui.textEdit.toPlainText()
            name = self.ui.card_name.text()
            self.parent().card.set_card_tip(structure.Card_tip(int(number), bool(state), str(description), str(name)))
            print(self.parent().card.get_card_tip())
            self.parent().reload_curr_tip()
            self.close()
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в TipCardForm", self).show()


class PointCardForm(CardForm):
    def __init__(self, parent=None):
        super().__init__(point_card_form, parent)
        self.ui.card_score_label.setText("Количество очков для варианта № " + str(len(self.parent().card.get_cards_point()) + 1))

    def save_n_next(self):
        try:
            number_card_history = self.parent().card.get_number()
            possible_answer = len(self.parent().card.get_cards_point()) + 1
            point = self.ui.card_score.text()
            self.parent().card.get_cards_point().append(structure.Card_point(int(number_card_history), int(possible_answer), int(point)))
            print(self.parent().card.get_cards_point())
            self.parent().reload_curr_points()
            self.ui.card_score.setText("")
            self.ui.card_score_label.setText("Количество очков для варианта № " + str(len(self.parent().card.get_cards_point()) + 1))
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в PointCardForm", self).show()

    def save_n_close(self):
        try:
            number_card_history = self.parent().card.get_number()
            possible_answer = len(self.parent().card.get_cards_point()) + 1
            point = self.ui.card_score.text()
            self.parent().card.get_cards_point().append(structure.Card_point(int(number_card_history), int(possible_answer), int(point)))
            print(self.parent().card.get_cards_point())
            self.parent().reload_curr_points()
            self.close()
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в PointCardForm", self).show()


class HistoryCardForm(CardForm):
    def __init__(self, parent=None):
        super().__init__(history_card_form, parent)
        self.ui.create_n_continue_but.clicked.connect(self.create_n_continue)
        self.ui.new_choice_but.clicked.connect(self.new_choice_init)
        self.ui.new_tip_card_but.clicked.connect(self.new_tip_card_init)
        self.ui.new_point_card_but.clicked.connect(self.new_point_card_init)
        parent_coords = self.parent().geometry().getRect()
        old_coords = self.geometry().getRect()
        self.setGeometry(QtCore.QRect(parent_coords[0], parent_coords[1], old_coords[2] // 2, old_coords[3]))
        self.card = None

    def create_n_continue(self):
        try:
            number = self.ui.card_number.text()
            state = self.ui.open_radio.isChecked()
            description = self.ui.textEdit.toPlainText()
            prescription = self.ui.card_prescription.text()
            scene = self.ui.card_scene.text()
            valid_date = self.ui.card_valid_date.text()
            self.card = structure.History_card(
                int(number), bool(state), str(description), str(prescription), str(scene), str(valid_date), [], None, [])
            print(self.card)
            old_coords = self.geometry().getRect()
            self.setGeometry(QtCore.QRect(old_coords[0] - (old_coords[2] // 2), old_coords[1], old_coords[2] * 2, old_coords[3]))
            self.ui.create_n_continue_but.hide()
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в HistoryCardForm", self).show()

    def new_choice_init(self):
        try:
            choice_window = ChoiceForm(self)
            choice_window.show()
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в HistoryCardForm", self).show()

    def reload_curr_choices(self):
        try:
            self.ui.curr_choices.setText("\n".join(map(str, self.card.get_choices())))
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в HistoryCardForm", self).show()

    def new_tip_card_init(self):
        try:
            tip_card_window = TipCardForm(self)
            tip_card_window.show()
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в HistoryCardForm", self).show()

    def reload_curr_tip(self):
        try:
            self.ui.curr_tip.setText(str(self.card.get_card_tip()))
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в HistoryCardForm", self).show()

    def new_point_card_init(self):
        try:
            point_card_window = PointCardForm(self)
            point_card_window.show()
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в HistoryCardForm", self).show()

    def reload_curr_points(self):
        try:
            print(self.card.get_cards_point()[0])
            self.ui.curr_points.setText("\n".join(map(str, self.card.get_cards_point())))
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в HistoryCardForm", self).show()

    def save_n_next(self):
        try:
            self.ui.card_number.setText("")
            self.ui.textEdit.setText("")
            self.ui.card_prescription.setText("")
            self.ui.card_scene.setText("")
            self.ui.card_valid_date.setText("")
            self.ui.curr_choices.setText("Нет вариантов ответа")
            self.ui.curr_tip.setText("Нет карты подсказки")
            self.ui.curr_points.setText("Нет карты подсказки")
            print(self.card)
            self.card.write_to_bd()
            self.card = None
            parent_coords = self.parent().geometry().getRect()
            old_coords = self.geometry().getRect()
            self.setGeometry(QtCore.QRect(parent_coords[0], parent_coords[1], old_coords[2] // 2, old_coords[3]))
            self.ui.create_n_continue_but.show()
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в HistoryCardForm", self).show()

    def save_n_close(self):
        try:
            print(self.card)
            self.card.write_to_bd()
            self.close()
        except BaseException:
            print(BaseException)
            ErrorMessage("Ошибка произошла в HistoryCardForm", self).show()

class AddCardForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = add_card.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.new_rule_card_but.clicked.connect(self.new_rule_card_init)
        self.ui.new_history_card_but.clicked.connect(self.new_history_card_init)
        self.ui.close_but.clicked.connect(self.close_ev)

    def new_rule_card_init(self):
        rule_card_window = RuleCardForm(self)
        rule_card_window.show()

    def new_history_card_init(self):
        history_card_window = HistoryCardForm(self)
        history_card_window.show()

    def close_ev(self):
        self.close()


if __name__=="__main__":
    structure.create_all_bd()
    app = QtWidgets.QApplication(sys.argv)
    add_card_window = AddCardForm()
    add_card_window.show()
    sys.exit(app.exec_())
