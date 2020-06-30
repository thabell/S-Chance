import sqlite3


class Card:  # Класс карты с текстом
    def __init__(self, number, state, description):
        self.number = number  # Номер карты
        self.state = state  # Открыта или закрыта(прочитана или непрочитана)
        self.description = description  # Надпись на самой карте

    def __str__(self):
        return '\nНомер карты: ' + str(
            self.number) + '\nСтатус карты: ' + self.state + '\nОписание: ' + self.description

    def get_number(self):
        return self.number

    def get_state(self):
        return self.state

    def get_description(self):
        return self.description

    @staticmethod
    def create_bd():  # Создание бд для класса Card
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS cards('
                    'number INTEGER,'
                    'state INTEGER,'
                    'description TEXT)')
        cur.close()
        con.close()

    @staticmethod
    def read_from_bd():  # Чтение экземпляров класса Card из бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM cards')
        cardlist_in_db = cur.fetchall()
        cards_list = []
        for card in cardlist_in_db:
            number = card[0]
            state = card[1]
            description = card[2]
            cards_list.append(Card(number, state, description))
        cur.close()
        con.close()
        return cards_list

    def write_to_bd(self):  # Запись экземпляров класса Card в бд
        list_to_add = []
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        state = self.get_state()
        list_to_add.append(state)
        description = self.get_description()
        list_to_add.append(description)
        cur.execute('INSERT INTO cards VALUES(?, ?)', list_to_add)
        con.commit()
        cur.close()
        con.close()


class History_card(Card):  # Класс Карта истории
    def __init__(self, number, state, description, prescription, scene, date, choices, card_tip, cards_point):
        super().__init__(number, state, description)
        self.prescription = prescription  # Давность действия
        self.scene = scene  # Место действия
        self.date = date  # Дата действия
        self.choices = choices  # Массив с вариантами выбора
        self.card_tip = card_tip  # Карта подсказки
        self.cards_point = cards_point  # Массив с картами судьбы

    def __str__(self):
        ans1 = '\nВарианты ответов: '
        ans2 = '\nКарта подсказки: '
        ans3 = '\nКарты судьбы: '
        for choice in self.choices:
            ans1 += str(choice[0]) + ') ' + str(choice[1]) + ' '
        for card in self.card_tip:
            ans2 += 'state card_tip: ' + str(card[0]) + ', text: ' + str(card[1]) + ', name: ' + str(card[2])
        for card in self.cards_point:
            ans3 += str(card[0]) + ') ' + str(card[1]) + ' '
        return super().__str__() + '\nДавность действия:' + self.prescription + '\nМесто действия: ' + self.scene + '\nДата действия: ' + self.date + 'г.' + ans1 + ans2 + ans3

    def get_prescription(self):
        return self.prescription

    def get_scene(self):
        return self.scene

    def get_date(self):
        return self.date

    def get_choices(self):
        return self.choices

    def get_card_tip(self):
        return self.card_tip

    def get_cards_point(self):
        return self.cards_point

    @staticmethod
    def create_bd():  # Создание бд для класса History_card
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS history_cards('
                    'number INTEGER, '
                    'state INTEGER, '
                    'description TEXT, '
                    'prescription TEXT, '
                    'scene TEXT, '
                    'date TEXT)')
        cur.close()
        con.close()

    @staticmethod
    def read_from_bd():  # Чтение экземпляров класса History_card из бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM history_cards')
        cardlist_in_db = cur.fetchall()
        history_cards_list = []
        for card in cardlist_in_db:
            number = card[0]
            state = card[1]
            description = card[2]
            prescription = card[3]
            scene = card[4]
            date = card[5]
            cur.execute(
                'SELECT choices.possible_answer, choices.text FROM history_cards INNER JOIN choices ON history_cards.number = choices.number_card_history')
            choices = cur.fetchall()
            cur.execute(
                'SELECT cards_point.possible_answer, cards_point.point FROM history_cards INNER JOIN cards_point ON history_cards.number = cards_point.number_card_history')
            cards_point = cur.fetchall()
            cur.execute(
                'SELECT cards_tip.state, cards_tip.description, cards_tip.name FROM history_cards INNER JOIN cards_tip ON history_cards.number = cards_tip.number_card_history')
            card_tip = cur.fetchall()
            history_cards_list.append(
                History_card(number, state, description, prescription, scene, date, choices, card_tip, cards_point))
        cur.close()
        con.close()
        return history_cards_list

    def write_to_bd(self):  # Запись экземпляров класса History_card в бд
        list_to_add = []
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        list_to_add.append(self.get_number())
        list_to_add.append(self.get_state())
        list_to_add.append(self.get_description())
        list_to_add.append(self.get_prescription())
        list_to_add.append(self.get_scene())
        list_to_add.append(self.get_date())
        cur.execute('INSERT INTO history_cards VALUES(?, ?, ?, ?, ?, ?)', list_to_add)
        con.commit()
        cur.close()
        con.close()
        choices = self.get_choices()
        for choice in choices:
            choice.write_to_bd()
        card_tip = self.get_card_tip()
        card_tip.write_to_bd()
        cards_point = self.get_cards_point()
        for card in cards_point:
            card.write_to_bd()


# TODO object history_card in read_from_bd_history_cards from history_cards with choices from history_choice_item
# TODO object get history_card by id

class Card_tip(Card):  # Класс Карт подсказок
    def __init__(self, number_card_history, state, description, name):
        super().__init__(number_card_history, state, description)
        self.number_card_history = number_card_history
        self.name = name  # Название подсказки

    def __str__(self):
        return super().__str__() + '\nНазвание подсказки: ' + self.name

    def get_number_card_history(self):
        return self.number_card_history

    def get_name(self):
        return self.name

    @staticmethod
    def create_bd():  # Создание бд для класса Card_tip
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS cards_tip('
                    'state INTEGER,'
                    'description TEXT,'
                    'name TEXT,'
                    'number_card_history INTEGER,'
                    'FOREIGN KEY (number_card_history) REFERENCES history_cards (number))')
        cur.close()
        con.close()

    @staticmethod
    def read_from_bd():  # Чтение экземпляров класса Card_tip из бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM cards_tip')
        cardslist_in_bd = cur.fetchall()
        cards_tip_list = []
        for card in cardslist_in_bd:
            number_card_history = card[0]
            state = card[1]
            description = card[2]
            name = card[3]
            cards_tip_list.append(Card_tip(number_card_history, state, description, name))
        cur.close()
        con.close()
        return cards_tip_list

    def write_to_bd(self):  # Запись экземпляров класса Card_tip в бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        state = self.get_state()
        description = self.get_description()
        name = self.get_name()
        cur.execute('INSERT INTO cards_tip VALUES(?, ?, ?, ?)',
                    [self.get_number_card_history(), state, description, name])
        con.commit()
        cur.close()
        con.close()


class Card_point:  # Класс Карт судьбы
    def __init__(self, number_card_history, possible_answer, point):
        self.number_card_history = number_card_history  # Номер карты истории
        self.possible_answer = possible_answer  # Выбранный вариант ответа
        self.point = point  # Количество очков

    def __str__(self):
        return '\nНомер карты истории: ' + str(
            self.number_card_history) + '\nВыбранный вариант ответа: ' + self.possible_answer + '\nКоличество очков: ' + str(
            self.point)

    def get_number_card_history(self):
        return self.number_card_history

    def get_possible_answer(self):
        return self.possible_answer

    def get_point(self):
        return self.point

    @staticmethod
    def create_bd():  # Создание бд для класса Card_point
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS cards_point('
                    'possible_answer TEXT,'
                    'point INTEGER,'
                    'number_card_history INTEGER,'
                    'FOREIGN KEY(number_card_history) REFERENCES history_cards(number))')
        cur.close()
        con.close()

    @staticmethod
    def read_from_bd():  # Чтение экземпляров класса Card_point из бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM cards_point')
        cardlist_in_db = cur.fetchall()
        cards_point_list = []
        for card in cardlist_in_db:
            number_card_history = card[0]
            possible_answer = card[1]
            point = card[2]
            cards_point_list.append(Card_point(number_card_history, possible_answer, point))
        cur.close()
        con.close()
        return cards_point_list

    def write_to_bd(self):  # Запись экземпляров класса Card_point в бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        possible_answer = self.get_possible_answer()
        point = self.get_point()
        cur.execute('INSERT INTO cards_point VALUES(?, ?, ?)', [self.get_number_card_history(), possible_answer, point])
        con.commit()
        cur.close()
        con.close()


class Choices:  # Класс вариантов ответа
    def __init__(self, number_card_history, possible_answer, text):
        self.number_card_history = number_card_history  # Номер карты истории
        self.possible_answer = possible_answer  # Вариант ответа
        self.text = text  # Текст варианта ответа

    def __str__(self):
        return '\nНомер карты истории: ' + str(
            self.number_card_history) + '\nВариант ответа: ' + self.possible_answer + '\nТекст варианта ответа: ' + self.text

    def get_number_card_history(self):
        return self.number_card_history

    def get_possible_answer(self):
        return self.possible_answer

    def get_text(self):
        return self.text

    @staticmethod
    def create_bd():  # Создание бд для класса Choices
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS choices('
                    'possible_answer TEXT,'
                    'text INTEGER,'
                    'number_card_history INTEGER,'
                    'FOREIGN KEY (number_card_history) REFERENCES history_cards (number))')
        cur.close()
        con.close()

    @staticmethod
    def read_from_bd():  # Чтение экземпляров класса Choices из бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM choices')
        cardlist_in_db = cur.fetchall()
        choices_list = []
        for card in cardlist_in_db:
            number_card_history = card[0]
            possible_answer = card[1]
            text = card[2]
            choices_list.append(Choices(number_card_history, possible_answer, text))
        cur.close()
        con.close()
        return choices_list

    def write_to_bd(self):  # Запись экземпляров класса Choices в бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        num = self.number_card_history()
        possible_answer = self.get_possible_answer()
        text = self.get_text()
        cur.execute('INSERT INTO choices VALUES(?, ?, ?)', [num, possible_answer, text])
        con.commit()
        cur.close()
        con.close()


def create_all_bd():
    Card.create_bd()
    History_card.create_bd()
    Card_tip.create_bd()
    Card_point.create_bd()
    Choices.create_bd()


if __name__ == "__main__":
    create_all_bd()
    print('Хотите ввести новое значение?[0/1]:', end=' ')
    ans = int(input())
    if ans == 1:
        choice = True
    else:
        choice = False
    while choice:
        print('Какого типа карту хотите добавить?[Card/History_card/Card_tip/Card_point/Choices]', end=' ')
        ans = input()
        if ans == 'Card':
            print('number  # Номер карты: ', end='')
            number = input()
            print('state  # Открыта или закрыта: ', end='')
            state = input()
            print('description  # Надпись на самой карте: ', end='')
            description = input()
            card = Card(number, state, description)
            card.write_to_bd()
        elif ans == 'Card_tip':
            print('number_card_history  # Номер карты истории: ', end='')
            number_card_history = int(input())
            print('state  # Открыта или закрыта: ', end='')
            state = input()
            print('description  # Надпись на самой карте: ', end='')
            description = input()
            print('name  # Название подсказки: ', end='')
            name = input()
            card_tip = Card_tip(number_card_history, state, description, name)
            card_tip.write_to_bd()
        elif ans == 'History_card':
            print('number  # Номер карты: ', end='')
            number = int(input())
            print('state  # Открыта или закрыта: ', end='')
            state = input()
            print('description  # Надпись на самой карте: ', end='')
            description = input()
            print('prescription  # Давность действия: ', end='')
            prescription = input()
            print('scene  # Место действия: ', end='')
            scene = input()
            print('date  # Дата действия: ', end='')
            date = input()
            print('choices  # Массив с вариантами выбора: ', end='')
            choices = list(map(str, input().split()))
            print('card_tip  # Карта подсказки: ', end='')
            card_tip = input()
            print('cards_point  # Массив с картами судьбы: ', end='')
            cards_point = list(map(str, input().split()))
            history_card = History_card(number, state, description, prescription, scene, date, choices, card_tip,
                                        cards_point)
            history_card.write_to_bd()
        elif ans == 'Card_point':
            print('number_card_history  # Номер карты истории: ', end='')
            number_card_history = int(input())
            print('possible_answer  # Выбранный вариант ответа[A, B, C]: ', end='')
            possible_answer = input()
            print('point  # Количество очков: ', end='')
            point = int(input())
            card_point = Card_point(number_card_history, possible_answer, point)
            card_point.write_to_bd()
        elif ans == 'Choices':
            print('number_card_history  # Номер карты истории: ', end='')
            number_card_history = int(input())
            print('possible_answer  # Вариант ответа[A, B, C]: ', end='')
            possible_answer = input()
            print('text  # Текст варианта ответа: ', end='')
            text = input()
            card_point = Choices(number_card_history, possible_answer, text)
            card_point.write_to_bd()
    print('Хотите прочитать всю базу данных?[0/1]:', end=' ')
    ans = int(input())
    if ans == 1:
        cards_list = Card.read_from_bd()
        for i in cards_list:
            print(i)
        history_cards_list = History_card.read_from_bd()
        for i in history_cards_list:
            print(i)
        cards_tip_list = Card_tip.read_from_bd()
        for i in cards_tip_list:
            print(i)
        cards_point_list = Card_point.read_from_bd()
        for i in cards_point_list:
            print(i)
        choices_list = Card_point.read_from_bd()
        for i in choices_list:
            print(i)
