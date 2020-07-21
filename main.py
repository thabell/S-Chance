import sys
from time import sleep

import structure
import rule_card_form
import solution_card_form
import tip_card_form
import history_card_form
import choice_form
import point_card_form
import add_card
import error_message
import alert
import game_table

from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Alert(QtWidgets.QMainWindow):
    def __init__(self, mess="Содержание сообщения", parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = alert.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setText(mess)


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
        new_card = structure.RuleCard(int(number), int(state), str(description))
        new_card.write_to_bd()

    def save_n_close(self):
        number = self.ui.card_number.text()
        state = self.ui.open_radio.isChecked()
        description = self.ui.card_description.toPlainText()
        new_card = structure.RuleCard(int(number), int(state), str(description))
        new_card.write_to_bd()
        self.close()


class SolutionCardForm(CardForm):
    def __init__(self, parent=None):
        super().__init__(solution_card_form, parent)

    def save_n_next(self):
        number = self.ui.card_number.text()
        state = self.ui.open_radio.isChecked()
        description = self.ui.card_description.toPlainText()
        self.ui.card_description.setText("")
        self.ui.card_number.setText("")
        new_card = structure.SolutionCard(int(number), int(state), str(description))
        new_card.write_to_bd()

    def save_n_close(self):
        number = self.ui.card_number.text()
        state = self.ui.open_radio.isChecked()
        description = self.ui.card_description.toPlainText()
        new_card = structure.SolutionCard(int(number), int(state), str(description))
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
            self.ui.curr_points.setText("Нет карт очков (Судьбы)")
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
        self.ui.new_solution_card_but.clicked.connect(self.new_solution_card_init)
        self.ui.new_history_card_but.clicked.connect(self.new_history_card_init)
        self.ui.close_but.clicked.connect(self.close_ev)

    def new_rule_card_init(self):
        rule_card_window = RuleCardForm(self)
        rule_card_window.show()

    def new_solution_card_init(self):
        solution_card_window = SolutionCardForm(self)
        solution_card_window.show()

    def new_history_card_init(self):
        history_card_window = HistoryCardForm(self)
        history_card_window.show()

    def close_ev(self):
        self.close()

from enum import Enum
from threading import Thread
from functools import partial
from random import randint


class GameTableWindow(QtWidgets.QMainWindow):
    class Steps(Enum):
        RULE_OPEN = 1
        RULE_ROLL = 2
        HISTORY_OPEN = 3
        HISTORY_ROLL = 4
        HISTORY_TIP_OPEN = 5
        HISTORY_TIP_ROLL = 6
        BACK_TO_HISTORY = 7
        BACK_TO_HISTORY_ROLL = 8
        HISTORY_CHOOSE = 9
        HISTORY_CONFIRM_CHOOSE = 10
        HISTORY_CHOICE_ROLL = 11
        SOLUTION_OPEN = 12
        SOLUTION_ROLL = 13
        HIDE_IMIT_N_FINISH = 14

    class Imitation:
        sequence_sample = []
        queue = []
        rule_wraps_list = []
        rule_list = []
        opened_rule = -2
        not_opened_history_ixs = []
        curr_hist_ix = 0
        twelve_done = False
        opened_solution = -2

        @staticmethod
        def prepare_imitation(args):
            rule_list = args[0]
            solution_list = args[1]
            history_list = args[2]
            window = args[3]
            for i in range(len(rule_list) // 2):
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.RULE_OPEN)
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.RULE_ROLL)
            for i in range(min(10, len(history_list))):
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.HISTORY_OPEN)
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.HISTORY_ROLL)
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.HISTORY_TIP_OPEN)
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.HISTORY_TIP_ROLL)
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.BACK_TO_HISTORY)
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.BACK_TO_HISTORY_ROLL)
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.HISTORY_CHOOSE)
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.HISTORY_CONFIRM_CHOOSE)
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.HISTORY_CHOICE_ROLL)
            for i in range(len(solution_list) // 2):
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.SOLUTION_OPEN)
                GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.SOLUTION_ROLL)
            GameTableWindow.Imitation.sequence_sample.append(GameTableWindow.Steps.HIDE_IMIT_N_FINISH)
            GameTableWindow.Imitation.queue = GameTableWindow.Imitation.sequence_sample.copy()
            GameTableWindow.Imitation.not_opened_history_ixs = list(range(len(window.h_buts)))
            if len(GameTableWindow.Imitation.not_opened_history_ixs) > 1:
                GameTableWindow.Imitation.curr_hist_ix = GameTableWindow.Imitation.not_opened_history_ixs.pop(1)

        @staticmethod
        def imitation_step_ev(window):
            try:
                step = GameTableWindow.Imitation.queue.pop(0)
                if step == GameTableWindow.Steps.RULE_OPEN:
                    window.r_buts[GameTableWindow.Imitation.opened_rule + 2].click()
                    GameTableWindow.Imitation.opened_rule += 1
                    print("imitated RULE_OPEN step")
                    window.ui.imitation_log.setText("imitated RULE_OPEN step")
                    sleep(1)
                elif step == GameTableWindow.Steps.RULE_ROLL:
                    window.ui.flip_the_card_but.click()
                    print("imitated RULE_ROLL step")
                    window.ui.imitation_log.setText("imitated RULE_ROLL step")
                    sleep(1)
                elif step == GameTableWindow.Steps.HISTORY_OPEN:
                    print("imitated HISTORY_OPEN step")
                    window.ui.imitation_log.setText("imitated HISTORY_OPEN step")
                    if GameTableWindow.Result.history_rest > 0:
                        # рандом тут, массив с индексами, оттуда попаются рандомно, и потом по этому попнотому обращение
                        # 12ю первой открываем
                        if GameTableWindow.Imitation.twelve_done:
                            GameTableWindow.Imitation.curr_hist_ix = GameTableWindow.Imitation.not_opened_history_ixs.pop(randint(0, len(GameTableWindow.Imitation.not_opened_history_ixs) - 1))
                        else:
                            GameTableWindow.Imitation.twelve_done = True
                        window.h_buts[GameTableWindow.Imitation.curr_hist_ix].click()
                        sleep(1)
                    else:
                        print("All history cards are opened, so nothing changed")
                elif step == GameTableWindow.Steps.HISTORY_ROLL:
                    print("imitated HISTORY_ROLL step")
                    window.ui.imitation_log.setText("imitated HISTORY_ROLL step")
                    if GameTableWindow.Result.history_rest > 0:
                        window.ui.flip_the_card_but.click()
                        sleep(1)
                    else:
                        print("All history cards are opened, so nothing changed")
                elif step == GameTableWindow.Steps.HISTORY_TIP_OPEN:
                    print("imitated HISTORY_TIP_OPEN step")
                    window.ui.imitation_log.setText("imitated HISTORY_TIP_OPEN step")
                    if GameTableWindow.Result.history_rest > 0 and GameTableWindow.Result.tip_rest > 0:
                        # подсказка открывается для открытой перед этим карты истории
                        window.t_buts[GameTableWindow.Imitation.curr_hist_ix].click()
                        sleep(1)
                    else:
                        print("All tip cards are opened or all history cards are opened, so nothing changed")
                elif step == GameTableWindow.Steps.HISTORY_TIP_ROLL:
                    print("imitated HISTORY_TIP_ROLL step")
                    window.ui.imitation_log.setText("imitated HISTORY_TIP_ROLL step")
                    if GameTableWindow.Result.history_rest > -1 and GameTableWindow.Result.tip_rest > 0:
                        window.ui.flip_the_card_but.click()
                        sleep(1)
                    else:
                        print("All tip cards are opened or all history cards are opened, so nothing changed")
                elif step == GameTableWindow.Steps.BACK_TO_HISTORY:
                    print("imitated BACK_TO_HISTORY step")
                    window.ui.imitation_log.setText("imitated BACK_TO_HISTORY step")
                    if GameTableWindow.Result.history_rest > -1 and GameTableWindow.Result.tip_rest > 0:
                        window.h_buts[GameTableWindow.Imitation.curr_hist_ix].click()
                        sleep(1)
                    else:
                        print("All tip cards are opened or all history cards are opened, so nothing changed")
                elif step == GameTableWindow.Steps.BACK_TO_HISTORY_ROLL:
                    print("imitated BACK_TO_HISTORY_ROLL step")
                    window.ui.imitation_log.setText("imitated BACK_TO_HISTORY_ROLL step")
                    if GameTableWindow.Result.history_rest > -1 and GameTableWindow.Result.tip_rest > 0:
                        window.ui.flip_the_card_but.click()
                        sleep(1)
                    else:
                        print("All tip cards are opened or all history cards are opened, so nothing changed")
                elif step == GameTableWindow.Steps.HISTORY_CHOOSE:
                    print("imitated HISTORY_CHOOSE step")
                    window.ui.imitation_log.setText("imitated HISTORY_CHOOSE step")
                    if GameTableWindow.Result.history_rest > -1:
                        try:
                            window.ch_buts[randint(0, 2)].click()
                            GameTableWindow.Imitation.no_choose = False
                            sleep(1)
                        except BaseException:
                            print("Nothing to choose")
                            GameTableWindow.Imitation.no_choose = True
                    else:
                        print("All history cards are opened, so nothing changed")
                elif step == GameTableWindow.Steps.HISTORY_CONFIRM_CHOOSE:
                    print("imitated HISTORY_CONFIRM_CHOOSE step")
                    window.ui.imitation_log.setText("imitated HISTORY_CONFIRM_CHOOSE step")
                    if GameTableWindow.Result.history_rest > -1 and not GameTableWindow.Imitation.no_choose:
                        window.conf_ch_but.click()
                        sleep(1)
                    else:
                        print("All history cards are opened or no choose, so nothing changed")
                elif step == GameTableWindow.Steps.HISTORY_CHOICE_ROLL:
                    print("imitated HISTORY_CHOICE_ROLL step")
                    window.ui.imitation_log.setText("imitated HISTORY_CHOICE_ROLL step")
                    if GameTableWindow.Result.history_rest > -1 and not GameTableWindow.Imitation.no_choose:
                        window.ui.flip_the_card_but.click()
                        sleep(1)
                    else:
                        print("All history cards are opened or no choose, so nothing changed")
                    if GameTableWindow.Result.history_rest == 0:
                        GameTableWindow.Result.history_rest -= 1  # это все было для последней карты. ведь она
                        # открыта, значит 0 карт истории. однако подсказку и выбор еще надо открыть
                elif step == GameTableWindow.Steps.SOLUTION_OPEN:
                    window.s_buts[GameTableWindow.Imitation.opened_solution + 2].click()
                    GameTableWindow.Imitation.opened_solution += 1
                    print("imitated SOLUTION_OPEN step")
                    window.ui.imitation_log.setText("imitated SOLUTION_OPEN step")
                    sleep(1)
                elif step == GameTableWindow.Steps.SOLUTION_ROLL:
                    window.ui.flip_the_card_but.click()
                    print("imitated SOLUTION_ROLL step")
                    window.ui.imitation_log.setText("imitated SOLUTION_ROLL step")
                    sleep(1)
                elif step == GameTableWindow.Steps.HIDE_IMIT_N_FINISH:
                    # Alert("Имитация закончена, спасибо за внимание!", window).show()
                    print("imitated HIDE_IMIT_N_FINISH step")
                    window.ui.imitation_log.setText("Имитация закончена, спасибо за внимание!")
                else:
                    print("Error. Not supported step.")
                window.repaint()
            except BaseException:
                print("Error in imitation step. Perhaps you have interrupted the process.")

        @staticmethod
        def whole_imitation_ev(window):
            window.ui.imitation_step.hide()
            window.ui.whole_imitation.hide()
            window.ui.imitation_log.show()
            window.new_thread = Thread(target=GameTableWindow.Imitation.whole_imitation_circle, args=(window,))
            window.new_thread.daemon = True
            window.new_thread.start()

        @staticmethod
        def whole_imitation_circle(window):
            while len(GameTableWindow.Imitation.queue) > 0:
                GameTableWindow.Imitation.imitation_step_ev(window)

    class Result:
        numbers = list(range(1, 14))
        states = ["Закрыта"] * 14
        tip_states = ["Закрыта"] * 14
        points = [0] * 14
        history_rest = 10
        tip_rest = 5
        solution_block = None

        @staticmethod
        def block_all_release_solution(window):
            print("blocked, released")
            # TODO открыть первую карту решения, когда будет сделан последний выбор. типа здесь чек вешать,
            #  что открыты все. и а если тринадцатая? короче надо ждать сигнала, ждем выбор или не ждем
            #  типа если тринадцатый номер открыт сейчас, то не ждем, иначе ждем...

            for el in window.ui.history_cards_box.children():
                try:
                    name = int(el.objectName())
                    check = False
                    for i in GameTableWindow.Result.numbers:
                        if name == i:
                            check = True
                            break
                    if check and GameTableWindow.Result.states[name] == "Закрыта":
                        window.ui.history_cards_box.findChild(QtWidgets.QWidget, str(name)).hide()
                except BaseException:
                    pass
            GameTableWindow.Result.solution_block.hide()
            GameTableWindow.Result.block_tips(window)

        @staticmethod
        def block_tips(window):
            for el in window.ui.tip_cards_box.children():
                try:
                    name = int(el.objectName())
                    check = False
                    for i in GameTableWindow.Result.numbers:
                        if name == i:
                            check = True
                            break
                    if check and GameTableWindow.Result.tip_states[name] == "Закрыта":
                        window.ui.tip_cards_box.findChild(QtWidgets.QWidget, str(name)).hide()
                except BaseException:
                    pass

        @staticmethod
        def get_header():
            return '{:-^35}'.format('') + "\n|" + '{:^7}'.format('№') + "|" + '{:^11}'.format(
                'Статус') + "|" + '{:^9}'.format('Баллы') + "|\n" + '{:-^35}'.format('')

        @staticmethod
        def get_line(n, status, points):
            return "\n|" + '{:^9}'.format(str(n)) + "|" + '{:^9}'.format(status) + "|" + '{:^13}'.format(
                str(points)) + "|\n" + '{:-^35}'.format('')

        @staticmethod
        def get_footer(score):
            return "\n|" + '{:^23}'.format(str("Итого")) + "|" + '{:^16}'.format(str(score)) + "|\n" + '{:-^35}'.format(
                '')

        @staticmethod
        def paint_res(window):
            text = GameTableWindow.Result.get_header()
            for i in GameTableWindow.Result.numbers:
                text += GameTableWindow.Result.get_line(i, GameTableWindow.Result.states[i], GameTableWindow.Result.points[i])
            text += GameTableWindow.Result.get_footer(sum(GameTableWindow.Result.points))
            window.ui.results_table.setText(text)

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = game_table.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add_cards_but.triggered.connect(self.add_card_init)

        self.ui.action_card_box.hide()
        self.ui.rule_cards_box.hide()
        self.ui.solution_cards_box.hide()
        self.ui.point_cards_box.hide()
        self.ui.tip_cards_box.hide()
        self.ui.history_cards_box.hide()
        self.ui.thanks.hide()

        self.ui.spread_the_cards_but.clicked.connect(self.spread_the_cards_ev)

        self.ui.flip_the_card_but.clicked.connect(partial(self.open_ev, self.ui.action_card_box))

        GameTableWindow.Result.paint_res(self)
        self.ui.res_wrapper.hide()

        self.ui.imitation_step.clicked.connect(partial(GameTableWindow.Imitation.imitation_step_ev, self))
        self.ui.imitation_step.hide()

        self.ui.whole_imitation.clicked.connect(partial(GameTableWindow.Imitation.whole_imitation_ev, self))
        self.ui.whole_imitation.hide()
        self.ui.imitation_log.hide()

    def add_card_init(self):
        add_card_window = AddCardForm(self)
        add_card_window.show()

    def spread_the_cards_ev(self):
        self.ui.res_wrapper.show()
        self.ui.greeting_box.hide()
        rule_box = self.ui.rule_cards_box
        solution_box = self.ui.solution_cards_box
        point_box = self.ui.point_cards_box
        tip_box = self.ui.tip_cards_box
        history_box = self.ui.history_cards_box
        rule_box.show()
        solution_box.show()
        point_box.show()
        tip_box.show()
        history_box.show()
        structure.create_all_bd()
        decks = structure.init_from_bd_n_sort_by_decks()
        # [rule_cards_list, solution_cards_list, history_cards_list, cards_tip_list, cards_point_list, choices_list]
        rule_list = decks[0]
        solution_list = decks[1]
        history_list = decks[2]
        tip_list = decks[3]
        point_list = decks[4]
        choices_list = decks[5]

        rule_wraps_list = []
        for i in range(len(rule_list) - 1, -1, -1):
            rule_card_wrap = QtWidgets.QWidget(rule_box)
            rule_card_wrap.setGeometry(QtCore.QRect(20, 30, 140, 210))
            rule_card_wrap.setObjectName("rule_card_wrap")
            rule_card_wrap.show()
            rule_card = self.create_card(rule_card_wrap, "rule_card", QtCore.QRect(0, 0, 140, 210),
                             "border-image: url(:/img/static/vertical_front2.jpg) 0 0 0 0 stretch stretch;")
            rule_card.show()
            rule_text = self.create_text(
                rule_card_wrap, "rule_card_text", QtCore.QRect(20, 30, 100, 150),
                "font: 10pt 'Capitol Deco';", str(rule_list[i].get_number()) + "<br>" + rule_list[i].get_description()[0:70:] + "...")
            rule_text.show()
            new_but = QtWidgets.QPushButton(rule_card_wrap)
            new_but.setGeometry(QtCore.QRect(0, 0, 140, 210))
            new_but.setObjectName("rule_card_but")
            new_but.setCursor(QtCore.Qt.PointingHandCursor)
            new_but.setStyleSheet("border: none; background-color: transparent;")
            new_but.show()
            rule_wraps_list.append(rule_card_wrap)
        self.r_buts = []
        for i in range(len(rule_wraps_list) - 1, -1, -2):
            if i > 2:
                next_opn_ix = i - 2
            else:
                next_opn_ix = len(rule_wraps_list) - 1
            rule_wraps_list[i].findChild(QtWidgets.QPushButton, "rule_card_but").clicked.connect(
                partial(self.to_action_box_ev, [
                    [rule_wraps_list[i], rule_wraps_list[i - 1]],
                    [rule_wraps_list[next_opn_ix]],
                    [rule_list[len(rule_list) - 1 - i], rule_list[len(rule_list) - 1 - i + 1]]
                ]))
            self.r_buts.append(rule_wraps_list[i].findChild(QtWidgets.QPushButton, "rule_card_but"))

        self.h_buts = []
        self.t_buts = []
        for i in range(len(history_list) - 1, -1, -1):
            curr_box = history_box.children()[i]
            curr_box.setObjectName(str(history_list[i].get_number()))
            history_card = self.create_card(curr_box, "history_card", QtCore.QRect(0, 0, curr_box.geometry().getRect()[2], curr_box.geometry().getRect()[3]),
                                         "border-image: url(:/img/static/vertical_front1.jpg) 0 0 0 0 stretch stretch;")
            history_card.show()
            history_text = self.create_text(
                curr_box, "history_card_text", QtCore.QRect(3, 3, curr_box.geometry().getRect()[2] - 6, curr_box.geometry().getRect()[3] - 6),
                "font: 8pt 'Capitol Deco';",
                str(history_list[i].get_number()) + "\n" + history_list[i].get_prescription() + "\n" + history_list[i].get_scene())
            history_text.show()
            new_but = QtWidgets.QPushButton(curr_box)
            new_but.setGeometry(QtCore.QRect(0, 0, curr_box.geometry().getRect()[2], curr_box.geometry().getRect()[3]))
            new_but.setObjectName("history_card_but")
            new_but.setCursor(QtCore.Qt.PointingHandCursor)
            new_but.setStyleSheet("border: none; background-color: transparent;")
            new_but.show()
            new_but.clicked.connect(partial(self.to_action_box_ev, [
                    [],
                    [],
                    [history_list[i], history_list[i]]
                ]))
            self.h_buts.append(new_but)
            if history_list[i].get_card_tip():
                curr_tip = tip_box.children()[i]
                curr_tip.setObjectName(str(history_list[i].get_card_tip().get_number()))
                tip_card = self.create_card(curr_tip, "tip_card",
                                                QtCore.QRect(0, 0, curr_tip.geometry().getRect()[2],
                                                             curr_tip.geometry().getRect()[3]),
                                                "border-image: url(:/img/static/horisontal_front2.jpg) 0 0 0 0 stretch stretch;")
                tip_card.show()
                tip_text = self.create_text(
                    curr_tip, "tip_card_text",
                    QtCore.QRect(3, 3, curr_tip.geometry().getRect()[2] - 6, curr_tip.geometry().getRect()[3] - 6),
                    "font: 8pt 'Capitol Deco';",
                    str(history_list[i].get_card_tip().get_number()) + "\n" + history_list[i].get_card_tip().get_name()
                )
                tip_text.show()
                new_but = QtWidgets.QPushButton(curr_tip)
                new_but.setGeometry(
                    QtCore.QRect(0, 0, curr_tip.geometry().getRect()[2], curr_tip.geometry().getRect()[3]))
                new_but.setObjectName("tip_card_but")
                new_but.setCursor(QtCore.Qt.PointingHandCursor)
                new_but.setStyleSheet("border: none; background-color: transparent;")
                new_but.show()
                new_but.clicked.connect(partial(self.to_action_box_ev, [
                    [],
                    [curr_tip],
                    [history_list[i].get_card_tip(), history_list[i].get_card_tip()]
                ]))
                self.t_buts.append(new_but)
            if len(history_list[i].get_cards_point()) > 0:
                for j in range(len(history_list[i].get_cards_point())):
                    point_card_wrap = QtWidgets.QWidget(point_box)
                    point_card_wrap.setGeometry(QtCore.QRect(0, 30, point_box.geometry().getRect()[2], point_box.geometry().getRect()[3] - 30))
                    point_card_wrap.setObjectName(str(history_list[i].get_number()) + "_" + str(j + 1))
                    point_card_wrap.show()
                    point_card = self.create_card(point_card_wrap, "tip_card",
                                                QtCore.QRect(0, 0, point_card_wrap.geometry().getRect()[2],
                                                             point_card_wrap.geometry().getRect()[3]),
                                                "border-image: url(:/img/static/horisontal_front1.jpg) 0 0 0 0 stretch stretch;")
                    point_card.show()
                    point_text = self.create_text(
                        point_card_wrap, "point_card_text",
                        QtCore.QRect(3, 20, point_card_wrap.geometry().getRect()[2] - 6, point_card_wrap.geometry().getRect()[3] - 40),
                        "font: 14pt 'Capitol Deco';",
                        str(history_list[i].get_cards_point()[j].get_number_card_history()) + " — " + str(history_list[i].get_cards_point()[j].get_possible_answer())
                    )
                    point_text.show()

        solution_wraps_list = []
        for i in range(len(solution_list) - 1, -1, -1):
            solution_card_wrap = QtWidgets.QWidget(solution_box)
            solution_card_wrap.setGeometry(QtCore.QRect(20, 30, 140, 210))
            solution_card_wrap.setObjectName("solution_card_wrap")
            solution_card_wrap.show()
            solution_card = self.create_card(solution_card_wrap, "solution_card", QtCore.QRect(0, 0, 140, 210),
                             "border-image: url(:/img/static/vertical_front2.jpg) 0 0 0 0 stretch stretch;")
            solution_card.show()
            solution_text = self.create_text(
                solution_card_wrap, "solution_card_text", QtCore.QRect(20, 30, 100, 150),
                "font: 10pt 'Capitol Deco';", str(solution_list[i].get_number()) + "<br>" + solution_list[i].get_description()[0:70:] + "...")
            solution_text.show()
            new_but = QtWidgets.QPushButton(solution_card_wrap)
            new_but.setGeometry(QtCore.QRect(0, 0, 140, 210))
            new_but.setObjectName("solution_card_but")
            new_but.setCursor(QtCore.Qt.PointingHandCursor)
            new_but.setStyleSheet("border: none; background-color: transparent;")
            new_but.show()
            solution_wraps_list.append(solution_card_wrap)
        solution_block = QtWidgets.QLabel(solution_box)
        solution_block.setGeometry(QtCore.QRect(20, 30, 140, 210))
        solution_block.setStyleSheet("border-image: url(:/img/static/01.jpg) 0 0 0 0 stretch stretch;")
        solution_block.show()
        GameTableWindow.Result.solution_block = solution_block
        self.s_buts = []
        for i in range(len(solution_wraps_list) - 1, -1, -2):
            if i > 2:
                next_opn_ix = i - 2
            else:
                next_opn_ix = len(solution_wraps_list) - 1
            solution_wraps_list[i].findChild(QtWidgets.QPushButton, "solution_card_but").clicked.connect(
                partial(self.to_action_box_ev, [
                    [solution_wraps_list[i], solution_wraps_list[i - 1]],
                    [solution_wraps_list[next_opn_ix]],
                    [solution_list[len(solution_list) - 1 - i], solution_list[len(solution_list) - 1 - i + 1]]
                ]))
            self.s_buts.append(solution_wraps_list[i].findChild(QtWidgets.QPushButton, "solution_card_but"))

        GameTableWindow.Imitation.prepare_imitation([rule_list, solution_list, history_list, self])
        self.ui.imitation_step.show()
        self.ui.whole_imitation.show()

    def create_card(self, box, name, coords, style):
        new_card = QtWidgets.QLabel(box)
        new_card.setObjectName(name)
        new_card.setGeometry(coords)
        new_card.setStyleSheet(style)
        new_card.show()
        return new_card

    def create_text(self, box, name, coords, style, text):
        new_text = QtWidgets.QLabel(box)
        new_text.setObjectName(name)
        new_text.setGeometry(coords)
        new_text.setStyleSheet(style)
        new_text.setText(text)
        new_text.setAlignment(QtCore.Qt.AlignCenter)
        new_text.setWordWrap(True)
        return new_text

    def to_action_box_ev(self, args):  # args = [[hide], [show], [back, front]]
        print("to_action_box_ev")
        for el in args[0]:
            el.hide()
        for el in args[1]:
            el.show()

        action_box = self.ui.action_card_box
        action_box.show()
        action_card_back = action_box.findChild(QtWidgets.QWidget, "card_back")
        for ch in action_card_back.children():
            ch.deleteLater()
        action_card_front = action_box.findChild(QtWidgets.QWidget, "card_front")
        for ch in action_card_front.children():
            ch.deleteLater()
        if isinstance(args[2][0], structure.RuleCard):
            action_box.type_ = "RuleCard"
            img = QtWidgets.QLabel(action_card_back)
            img.setGeometry(QtCore.QRect(0, 0, action_card_back.geometry().getRect()[2],
                                              action_card_back.geometry().getRect()[3]))
            img.setStyleSheet("border-image: url(:/img/static/vertical_front2.jpg) 0 0 0 0 stretch stretch;")
            img.setObjectName("action_card_back_img")
            img.show()
            new_text = QtWidgets.QLabel(action_card_back)
            new_text.setObjectName("action_card_back_text")
            new_text.setGeometry(QtCore.QRect(50, 50, action_card_back.geometry().getRect()[2] - 100, action_card_back.geometry().getRect()[3] - 100))
            new_text.setStyleSheet("font: 12px 'Lato Regular'; color: #ffffff")
            new_text.setText(str(args[2][0].get_number()) + "<br>" + args[2][0].get_description())
            new_text.setAlignment(QtCore.Qt.AlignCenter)
            new_text.setWordWrap(True)
            new_text.show()
        elif isinstance(args[2][0], structure.History_card):
            action_box.type_ = "History_card"
            action_box.card_number = args[2][0].get_number()
            img = QtWidgets.QLabel(action_card_back)
            img.setGeometry(QtCore.QRect(0, 0, action_card_back.geometry().getRect()[2],
                                         action_card_back.geometry().getRect()[3]))
            img.setStyleSheet("border-image: url(:/img/static/vertical_front1.jpg) 0 0 0 0 stretch stretch;")
            img.setObjectName("action_card_back_img")
            img.show()
            new_text = QtWidgets.QLabel(action_card_back)
            new_text.setObjectName("action_card_back_text")
            new_text.setGeometry(QtCore.QRect(50, 50, action_card_back.geometry().getRect()[2] - 100,
                                              action_card_back.geometry().getRect()[3] - 100))
            new_text.setStyleSheet("font: 12px 'Lato Regular'; color: #ffffff")
            new_text.setText(str(args[2][0].get_number()) + "<br><br>" + args[2][0].get_prescription() + "<br><br><b>" + args[2][0].get_scene() + "</b><br><br>" + args[2][0].get_date())
            new_text.setAlignment(QtCore.Qt.AlignCenter)
            new_text.setWordWrap(True)
            new_text.show()
        elif isinstance(args[2][0], structure.Card_tip):
            action_box.type_ = "Card_tip"
            action_box.card_number = args[2][0].get_number()
            img = QtWidgets.QLabel(action_card_back)
            img.setGeometry(QtCore.QRect(0, action_card_back.geometry().getRect()[3] // 2 // 2, action_card_back.geometry().getRect()[2],
                                         action_card_back.geometry().getRect()[3] // 2))
            img.setStyleSheet("border-image: url(:/img/static/horisontal_front2.jpg) 0 0 0 0 stretch stretch;")
            img.setObjectName("action_card_back_img")
            img.show()
            new_text = QtWidgets.QLabel(action_card_back)
            new_text.setObjectName("action_card_back_text")
            new_text.setGeometry(QtCore.QRect(50, 50, action_card_back.geometry().getRect()[2] - 100,
                                              action_card_back.geometry().getRect()[3] - 100))
            new_text.setStyleSheet("font: 12px 'Lato Regular'; color: #ffffff")
            new_text.setText(str(args[2][0].get_number()) + "<br><br><b>" + args[2][0].get_name() + "</b>")
            new_text.setAlignment(QtCore.Qt.AlignCenter)
            new_text.setWordWrap(True)
            new_text.show()
        elif isinstance(args[2][0], structure.Card_point):
            action_box.type_ = "Card_point"
            img = QtWidgets.QLabel(action_card_back)
            img.setGeometry(QtCore.QRect(0, action_card_back.geometry().getRect()[3] // 2 // 2, action_card_back.geometry().getRect()[2],
                                         action_card_back.geometry().getRect()[3] // 2))
            img.setStyleSheet("border-image: url(:/img/static/horisontal_front1.jpg) 0 0 0 0 stretch stretch;")
            img.setObjectName("action_card_back_img")
            img.show()
            new_text = QtWidgets.QLabel(action_card_back)
            new_text.setObjectName("action_card_back_text")
            new_text.setGeometry(QtCore.QRect(50, 50, action_card_back.geometry().getRect()[2] - 100,
                                              action_card_back.geometry().getRect()[3] - 100))
            new_text.setStyleSheet("font: 18px 'Lato Regular'; color: #ffffff")
            new_text.setText("<b>" + str(args[2][0].get_number_card_history()) + " — " + str(args[2][0].get_possible_answer()) + "</b>")
            new_text.setAlignment(QtCore.Qt.AlignCenter)
            new_text.setWordWrap(True)
            new_text.show()
        elif isinstance(args[2][0], structure.SolutionCard):
            action_box.type_ = "SolutionCard"
            self.ui.thanks.show()
            img = QtWidgets.QLabel(action_card_back)
            img.setGeometry(QtCore.QRect(0, 0, action_card_back.geometry().getRect()[2],
                                              action_card_back.geometry().getRect()[3]))
            img.setStyleSheet("border-image: url(:/img/static/vertical_front2.jpg) 0 0 0 0 stretch stretch;")
            img.setObjectName("action_card_back_img")
            img.show()
            new_text = QtWidgets.QLabel(action_card_back)
            new_text.setObjectName("action_card_back_text")
            new_text.setGeometry(QtCore.QRect(50, 50, action_card_back.geometry().getRect()[2] - 100, action_card_back.geometry().getRect()[3] - 100))
            new_text.setStyleSheet("font: 12px 'Lato Regular'; color: #ffffff")
            new_text.setText(str(args[2][0].get_number()) + "<br>" + args[2][0].get_description())
            new_text.setAlignment(QtCore.Qt.AlignCenter)
            new_text.setWordWrap(True)
            new_text.show()
        action_card_back.show()

        if isinstance(args[2][1], structure.RuleCard):
            img = QtWidgets.QLabel(action_card_front)
            img.setGeometry(QtCore.QRect(0, 0, action_card_front.geometry().getRect()[2],
                                              action_card_back.geometry().getRect()[3]))
            img.setStyleSheet("border-image: url(:/img/static/vertical_front2.jpg) 0 0 0 0 stretch stretch;")
            img.setObjectName("action_card_back_img")
            img.show()
            new_text = QtWidgets.QLabel(action_card_front)
            new_text.setObjectName("action_card_back_text")
            new_text.setGeometry(QtCore.QRect(50, 50, action_card_front.geometry().getRect()[2] - 100, action_card_back.geometry().getRect()[3] - 100))
            new_text.setStyleSheet("font: 12px 'Lato Regular'; color: #ffffff")
            new_text.setText(str(args[2][1].get_number()) + "<br>" + args[2][1].get_description())
            new_text.setAlignment(QtCore.Qt.AlignCenter)
            new_text.setWordWrap(True)
            new_text.show()
        elif isinstance(args[2][1], structure.History_card):
            img = QtWidgets.QLabel(action_card_front)
            img.setGeometry(QtCore.QRect(0, 0, action_card_front.geometry().getRect()[2],
                                         action_card_back.geometry().getRect()[3]))
            img.setStyleSheet("border-image: url(:/img/static/vertical_back1.jpg) 0 0 0 0 stretch stretch;")
            img.setObjectName("action_card_back_img")
            img.show()
            new_text = QtWidgets.QLabel(action_card_front)
            new_text.setObjectName("action_card_back_text")
            new_text.setGeometry(QtCore.QRect(50, 35, action_card_front.geometry().getRect()[2] - 100,
                                              action_card_back.geometry().getRect()[3] - 70))
            new_text.setStyleSheet("font: 12px 'Lato Regular'; color: #ffffff")
            new_text.setText(str(args[2][1].get_number()) + "<br><br><br>" + args[2][1].get_prescription() + "<br><b>" + args[2][1].get_scene() + "</b><br>" + args[2][1].get_date() + "<br><br>" + args[2][1].get_description())
            new_text.setAlignment(QtCore.Qt.AlignHCenter)
            new_text.setWordWrap(True)
            new_text.show()
            self.ch_buts = []
            if len(args[2][1].choices) > 0:
                new_gr_box = QtWidgets.QWidget(action_card_front)
                new_gr_box.setObjectName("new_gr_box")
                new_gr_box.setGeometry(QtCore.QRect(55, action_card_back.geometry().getRect()[3] // 3 * 2 + 5, action_card_front.geometry().getRect()[2] - 110, action_card_back.geometry().getRect()[3] // 3 - 30))
                new_gr_box.setStyleSheet("font: 8px 'Lato Regular'; color: #ffffff; border: solid 2px #ffffff;")
                new_gr_box.show()
                for i in range(len(args[2][1].choices)):
                    text = QtWidgets.QLabel(new_gr_box)
                    text.setGeometry(QtCore.QRect(20, new_gr_box.geometry().getRect()[3] // 3 * i, new_gr_box.geometry().getRect()[2] - 20, new_gr_box.geometry().getRect()[3] // 3))
                    text.setStyleSheet("font: 11px 'Lato Regular'; color: #ffffff;")
                    text.setWordWrap(True)
                    text.setText(args[2][1].choices[i].get_text())
                    text.show()
                    var = QtWidgets.QRadioButton(new_gr_box)
                    var.setGeometry(QtCore.QRect(0, new_gr_box.geometry().getRect()[3] // 3 * i, new_gr_box.geometry().getRect()[2], new_gr_box.geometry().getRect()[3] // 3))
                    var.setObjectName(str(args[2][1].get_number()) + "_" + str(i + 1))
                    var.setStyleSheet("font: 11px 'Lato Regular'; color: #ffffff;")
                    var.show()
                    self.ch_buts.append(var)
                new_gr_box.findChild(QtWidgets.QRadioButton, str(args[2][1].get_number()) + "_1").setChecked(True)
            if args[2][1].get_number() != 12 and args[2][1].get_number() != 13:
                make_a_choice_but = QtWidgets.QPushButton(action_card_front)
                make_a_choice_but.setObjectName("make_a_choice_but")
                make_a_choice_but.setGeometry(QtCore.QRect(80, 450, 180, 50))
                make_a_choice_but.setStyleSheet("background-color: rgb(255, 255, 255);\nborder: none;\nborder-radius: 3px;\nfont: 63 11pt 'Lato Semibold';")
                make_a_choice_but.setText("Сделать выбор")
                make_a_choice_but.show()
                make_a_choice_but.clicked.connect(partial(self.make_a_choice_but_ev, args[2][1].get_cards_point()))
                self.conf_ch_but = make_a_choice_but
        elif isinstance(args[2][1], structure.Card_tip):
            img = QtWidgets.QLabel(action_card_front)
            img.setGeometry(QtCore.QRect(0, action_card_back.geometry().getRect()[3] // 2 // 2, action_card_front.geometry().getRect()[2],
                                         action_card_back.geometry().getRect()[3] // 2))
            img.setStyleSheet("border-image: url(:/img/static/gorizontal_back1.jpg) 0 0 0 0 stretch stretch;")
            img.setObjectName("action_card_back_img")
            img.show()
            new_text = QtWidgets.QLabel(action_card_front)
            new_text.setObjectName("action_card_back_text")
            new_text.setGeometry(QtCore.QRect(50, 50 + action_card_back.geometry().getRect()[3] // 2 // 2, action_card_front.geometry().getRect()[2] - 100,
                                              action_card_back.geometry().getRect()[3] // 2 - 100))
            new_text.setStyleSheet("font: 12px 'Lato Regular'; color: #ffffff")
            new_text.setText(str(args[2][1].get_number()) + "<br><br><b>" + args[2][1].get_name() + "</b><br><br>" + args[2][1].get_description())
            new_text.setAlignment(QtCore.Qt.AlignHCenter)
            new_text.setWordWrap(True)
            new_text.show()
        elif isinstance(args[2][1], structure.Card_point):
            img = QtWidgets.QLabel(action_card_front)
            img.setGeometry(QtCore.QRect(0, action_card_back.geometry().getRect()[3] // 2 // 2, action_card_front.geometry().getRect()[2],
                                         action_card_back.geometry().getRect()[3] // 2))
            img.setStyleSheet("border-image: url(:/img/static/gorizontal_back2.jpg) 0 0 0 0 stretch stretch;")
            img.setObjectName("action_card_back_img")
            img.show()
            new_text = QtWidgets.QLabel(action_card_front)
            new_text.setObjectName("action_card_back_text")
            new_text.setGeometry(QtCore.QRect(50, 50, action_card_front.geometry().getRect()[2] - 100,
                                              action_card_back.geometry().getRect()[3] - 100))
            new_text.setStyleSheet("font: 18px 'Lato Regular'; color: #ffffff")
            new_text.setText("<b>" + str(args[2][1].get_number_card_history()) + " — " + str(args[2][1].get_possible_answer()) + ": " + str(args[2][1].get_point()) + " балл(а)</b>")
            new_text.setAlignment(QtCore.Qt.AlignCenter)
            new_text.setWordWrap(True)
            new_text.show()
        elif isinstance(args[2][1], structure.SolutionCard):
            img = QtWidgets.QLabel(action_card_front)
            img.setGeometry(QtCore.QRect(0, 0, action_card_front.geometry().getRect()[2],
                                              action_card_back.geometry().getRect()[3]))
            img.setStyleSheet("border-image: url(:/img/static/vertical_front2.jpg) 0 0 0 0 stretch stretch;")
            img.setObjectName("action_card_back_img")
            img.show()
            new_text = QtWidgets.QLabel(action_card_front)
            new_text.setObjectName("action_card_back_text")
            new_text.setGeometry(QtCore.QRect(50, 50, action_card_front.geometry().getRect()[2] - 100, action_card_back.geometry().getRect()[3] - 100))
            new_text.setStyleSheet("font: 12px 'Lato Regular'; color: #ffffff")
            new_text.setText(str(args[2][1].get_number()) + "<br>" + args[2][1].get_description())
            new_text.setAlignment(QtCore.Qt.AlignCenter)
            new_text.setWordWrap(True)
            new_text.show()
        action_card_front.hide()

    def open_ev(self, action_box):
        print("rotate_ev")
        action_card_back = action_box.findChild(QtWidgets.QWidget, "card_back")
        action_card_front = action_box.findChild(QtWidgets.QWidget, "card_front")
        if action_card_back.isHidden():
            action_card_back.show()
            action_card_front.hide()
        else:
            if action_box.type_ == "History_card" and GameTableWindow.Result.states[action_box.card_number] != "Открыта":
                GameTableWindow.Result.states[action_box.card_number] = "Открыта"
                GameTableWindow.Result.paint_res(self)
                GameTableWindow.Result.history_rest -= 1
                self.ui.history_cards_box_title.setText("Карты Истории (осталось открыть " + str(GameTableWindow.Result.history_rest) + ")")
                if GameTableWindow.Result.history_rest < 1:
                    GameTableWindow.Result.block_all_release_solution(self)
                    # TODO если не 13 или 12, то не заканчивать, тогда закончить в событии make_a_choice_but_ev
            if action_box.type_ == "Card_tip" and GameTableWindow.Result.tip_states[action_box.card_number] != "Открыта":
                GameTableWindow.Result.tip_states[action_box.card_number] = "Открыта"
                GameTableWindow.Result.tip_rest -= 1
                self.ui.tip_cards_box_title.setText(
                    "Карты Подсказки (осталось открыть " + str(GameTableWindow.Result.tip_rest) + ")")
                if GameTableWindow.Result.tip_rest < 1:
                    GameTableWindow.Result.block_tips(self)

            action_card_back.hide()
            action_card_front.show()

    def make_a_choice_but_ev(self, curr_point_cards):
        print("make_a_choice_but_ev")
        action_box = self.ui.action_card_box
        if action_box.type_ == "History_card":
            gr_box = action_box.findChild(QtWidgets.QWidget, "new_gr_box")
            i = 10
            j = 1
            for el in gr_box.children():
                # print(el)
                if isinstance(el, QtWidgets.QRadioButton) and el.isChecked():
                    num = el.objectName().split("_")
                    i = int(num[0])
                    j = int(num[1])
            # print(i, j)
            point1 = self.ui.point_cards_box.findChild(QtWidgets.QWidget, str(i) + "_1")
            point2 = self.ui.point_cards_box.findChild(QtWidgets.QWidget, str(i) + "_2")
            point3 = self.ui.point_cards_box.findChild(QtWidgets.QWidget, str(i) + "_3")
            points = [point1, point2, point3]
            # print(curr_point_cards[j - 1])
            self.to_action_box_ev([points, [], [curr_point_cards[j - 1], curr_point_cards[j - 1]]])
            GameTableWindow.Result.points[i] = curr_point_cards[j - 1].get_point()
            GameTableWindow.Result.paint_res(self)

    # class Direction(Enum):
    #     FIRST_DECREASE = 1
    #     SECOND_GROW = 2

    # @staticmethod
    # def rotate_step(obj1, obj2):
        # # for i in range(steps):  # do while state != GameTableForm.Direction.SECOND_GROW or obj2.geometry().getRect()[0] < max_size
        # print("step")
        # old_coords1 = obj1.geometry().getRect()
        # new_coords1 = list(old_coords1)
        # old_coords2 = obj2.geometry().getRect()
        # new_coords2 = list(old_coords2)
        # if state == GameTableForm.Direction.FIRST_DECREASE:
        #     print("FIRST_DECREASE")
        #     if old_coords1[2] // 5 - 3 > 0:
        #         print("old_coords1[2] // 5 > 0")
        #         new_coords1[2] = old_coords1[2] // 5 * 4
        #         new_coords1[0] = old_coords1[0] + ((old_coords1[2] - new_coords1[2]) // 2)
        #     else:
        #         print("else")
        #         state = GameTableForm.Direction.SECOND_GROW
        #         new_coords2 = new_coords1
        #         obj1.hide()
        #         obj2.show()
        # else:
        #     print("SECOND_GROW")
        #     if old_coords2[2] + old_coords2[2] // 5 < max_size:
        #         print("old_coords2[2] + old_coords2[2] // 5 < max_size")
        #         new_coords2[2] = old_coords2[2] + old_coords2[2] // 5
        #         new_coords2[0] = old_coords2[0] - ((new_coords2[2] - old_coords2[2]) // 2)
        #     else:
        #         print("else")
        #         new_coords2[2] = max_size
        #         new_coords2[0] = old_coords2[0] - ((new_coords2[2] - old_coords2[2]) // 2)
        # obj1.setGeometry(QtCore.QRect(new_coords1[0], new_coords1[1], new_coords1[2], new_coords1[3]))
        # obj2.setGeometry(QtCore.QRect(new_coords2[0], new_coords2[1], new_coords2[2], new_coords2[3]))

    # def move_right_ev(self):
    #     print("move_ev")
    #     self.move_right(self.ui.label_2)

    # @staticmethod
    # def move_right(obj, steps=1, max_size=100):
    #     old_coords = obj.geometry().getRect()
    #     obj.setGeometry(QtCore.QRect(old_coords[0] + old_coords[0] // 10, old_coords[1], old_coords[2], old_coords[3]))

    def close_ev(self):
        self.close()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    game_table_window = GameTableWindow()
    game_table_window.show()
    sys.exit(app.exec_())
