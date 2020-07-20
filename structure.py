import sqlite3


class Card:  # Класс карты с текстом
    def __init__(self, number, state, description):
        self.number = number  # Номер карты
        self.state = state  # Открыта или закрыта(прочитана или непрочитана)
        self.description = description  # Надпись на самой карте

    def __str__(self):
        if self.state == 1:
            ans = 'Открыта'
        else:
            ans = 'Закрыта'
        return 'Текст № ' + str(self.number) + ': "' + str(self.description) + '" ' + ans

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
        cur.execute('SELECT * FROM cards ORDER BY number')
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
        list_to_add.append(self.get_number())
        state = self.get_state()
        list_to_add.append(state)
        description = self.get_description()
        list_to_add.append(description)
        cur.execute('INSERT INTO cards VALUES(?, ?, ?)', list_to_add)
        con.commit()
        cur.close()
        con.close()

class RuleCard(Card):
    def __init__(self, number, state, description):
        super().__init__(number, state, description)

    def __str__(self):
        return 'Правило № ' + str(self.number) + ': ' + str(self.description) + '. ' + ("Открыта" if bool(self.state) else "Закрыта")

    @staticmethod
    def create_bd():
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS rule_card('
                    'number INTEGER,'
                    'state INTEGER,'
                    'description TEXT)')
        cur.close()
        con.close()

    @staticmethod
    def read_from_bd():
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM rule_card ORDER BY number')
        bd_list = cur.fetchall()
        c_list = []
        print(bd_list)
        for card_ in bd_list:
            number_ = card_[0]
            state_ = card_[1]
            description_ = card_[2]
            c_list.append(RuleCard(number_, state_, description_))
        cur.close()
        con.close()
        return c_list

    def write_to_bd(self):
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        list_to_add = [self.get_number(), self.get_state(), self.get_description()]
        cur.execute('INSERT INTO rule_card VALUES(?, ?, ?)', list_to_add)
        con.commit()
        cur.close()
        con.close()

class SolutionCard(Card):
    def __init__(self, number, state, description):
        super().__init__(number, state, description)

    def __str__(self):
        return 'Решение № ' + str(self.number) + ': ' + str(self.description) + '. ' + ("Открыта" if bool(self.state) else "Закрыта")

    @staticmethod
    def create_bd():
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS solution_card('
                    'number INTEGER,'
                    'state INTEGER,'
                    'description TEXT)')
        cur.close()
        con.close()

    @staticmethod
    def read_from_bd():
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM solution_card ORDER BY number')
        bd_list = cur.fetchall()
        c_list = []
        for card_ in bd_list:
            number_ = card_[0]
            state_ = card_[1]
            description_ = card_[2]
            c_list.append(SolutionCard(number_, state_, description_))
        cur.close()
        con.close()
        return c_list

    def write_to_bd(self):
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        list_to_add = [self.get_number(), self.get_state(), self.get_description()]
        cur.execute('INSERT INTO solution_card VALUES(?, ?, ?)', list_to_add)
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
        ans1 = ', '
        ans2 = ', '
        for choice in self.choices:
            ans1 += str(choice) + ', '
        for card in self.cards_point:
            ans2 += str(card) + ', '
        return "История № " + str(self.number) + ". " + str(self.prescription) + ', ' + str(self.scene) + ', ' + str(self.date) + ': '\
               + str(self.description) + ("Открыта" if bool(self.state) else "Закрыта") + ans1 + str(self.card_tip) + ans2

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

    def set_card_tip(self, card_tip):
        self.card_tip = card_tip

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
        cur.execute('SELECT * FROM history_cards ORDER BY number')
        cardlist_in_db = cur.fetchall()
        history_cards_list = []
        for card in cardlist_in_db:
            number = card[0]
            state = card[1]
            description = card[2]
            prescription = card[3]
            scene = card[4]
            date = card[5]

            cur.execute('SELECT * FROM choices WHERE number_card_history=?  ORDER BY possible_answer', [(str(number))])
            choices_ = cur.fetchall()
            choices_list = []
            for choice in choices_:
                possible_answer = choice[0]
                text = choice[1]
                choices_list.append(Choices(possible_answer, text, number))

            cur.execute('SELECT * FROM cards_tip WHERE number=?', [(str(number))])
            card_tip_list = cur.fetchall()
            state_tip = card_tip_list[0][0]
            description_tip = card_tip_list[0][1]
            name_tip = card_tip_list[0][2]
            card_tip = Card_tip(number, state_tip, description_tip, name_tip)
            # TODO сделать инициализацию любой карты из массива: card_tip = Card_tip(card_tip_list)

            cur.execute('SELECT * FROM cards_point WHERE number_card_history=? ORDER BY possible_answer', [(str(number))])
            cards_point = cur.fetchall()
            cards_point_list = []
            for card in cards_point:
                possible_answer = card[0]
                point = card[1]
                cards_point_list.append(Card_point(number, possible_answer, point))

            history_cards_list.append(
                History_card(number, state, description, prescription, scene, date, choices_list, card_tip, cards_point_list))
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

class Choices:  # Класс вариантов ответа
    def __init__(self, possible_answer, text, number_card_history):
        self.possible_answer = possible_answer  # Вариант ответа
        self.text = text  # Текст варианта ответа
        self.number_card_history = number_card_history  # Номер карты истории

    def __str__(self):
        return 'Выбор № ' + str(self.number_card_history) + '.' + str(self.possible_answer) + ': ' + str(self.text)

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
                    'possible_answer INTEGER,'
                    'text TEXT,'
                    'number_card_history INTEGER,'
                    'FOREIGN KEY (number_card_history) REFERENCES history_cards (number))')
        cur.close()
        con.close()

    @staticmethod
    def read_from_bd():  # Чтение экземпляров класса Choices из бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM choices ORDER BY number_card_history')
        cardlist_in_db = cur.fetchall()
        choices_list = []
        for card in cardlist_in_db:
            possible_answer = card[0]
            text = card[1]
            number_card_history = card[2]
            choices_list.append(Choices(possible_answer, text, number_card_history))
        cur.close()
        con.close()
        return choices_list

    def write_to_bd(self):  # Запись экземпляров класса Choices в бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        num = self.get_number_card_history()
        possible_answer = self.get_possible_answer()
        text = self.get_text()
        cur.execute('INSERT INTO choices VALUES(?, ?, ?)', [possible_answer, text, num])
        con.commit()
        cur.close()
        con.close()


class Card_tip(Card):  # Класс Карт подсказок
    def __init__(self, number, state, description, name):
        super().__init__(number, state, description)
        self.name = name  # Название подсказки

    def __str__(self):
        if self.state == 1:
            ans = 'Открыта'
        else:
            ans = 'Закрыта'
        return 'Подсказка № ' + str(self.number) + ': ' + str(self.name) + '. "' + str(self.description) + '" ' + ans

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
                    'number INTEGER,'
                    'FOREIGN KEY (number) REFERENCES history_cards (number))')
        cur.close()
        con.close()

    @staticmethod
    def read_from_bd():  # Чтение экземпляров класса Card_tip из бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM cards_tip ORDER BY number')
        cardslist_in_bd = cur.fetchall()
        cards_tip_list = []
        for card in cardslist_in_bd:
            state = card[0]
            description = card[1]
            name = card[2]
            number = card[3]
            cards_tip_list.append(Card_tip(number, state, description, name))
        cur.close()
        con.close()
        return cards_tip_list

    def write_to_bd(self):  # Запись экземпляров класса Card_tip в бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        state = self.get_state()
        description = self.get_description()
        name = self.get_name()
        cur.execute('INSERT INTO cards_tip VALUES(?, ?, ?, ?)', [state, description, name, self.get_number()])
        con.commit()
        cur.close()
        con.close()


class Card_point:  # Класс Карт судьбы
    def __init__(self, number_card_history, possible_answer, point):
        self.number_card_history = number_card_history  # Номер карты истории
        self.possible_answer = possible_answer  # Выбранный вариант ответа
        self.point = point  # Количество очков

    def __str__(self):
        return 'Судьба № ' + str(self.number_card_history) + '.' + str(self.possible_answer) + ': принес ' + str(self.point) + ' очков'

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
                    'possible_answer INTEGER,'
                    'point INTEGER,'
                    'number_card_history INTEGER,'
                    'FOREIGN KEY(number_card_history) REFERENCES history_cards(number))')
        cur.close()
        con.close()

    @staticmethod
    def read_from_bd():  # Чтение экземпляров класса Card_point из бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        cur.execute('SELECT * FROM cards_point ORDER BY number_card_history')
        cardlist_in_db = cur.fetchall()
        cards_point_list = []
        for card in cardlist_in_db:
            possible_answer = card[0]
            point = card[1]
            number_card_history = card[2]
            cards_point_list.append(Card_point(number_card_history, possible_answer, point))
        cur.close()
        con.close()
        return cards_point_list

    def write_to_bd(self):  # Запись экземпляров класса Card_point в бд
        con = sqlite3.connect('./game_base.db')
        cur = con.cursor()
        possible_answer = self.get_possible_answer()
        point = self.get_point()
        cur.execute('INSERT INTO cards_point VALUES(?, ?, ?)', [possible_answer, point, self.get_number_card_history()])
        con.commit()
        cur.close()
        con.close()


def create_all_bd():
    Card.create_bd()
    History_card.create_bd()
    Card_tip.create_bd()
    Card_point.create_bd()
    Choices.create_bd()
    RuleCard.create_bd()
    SolutionCard.create_bd()

def init_from_bd_n_sort_by_decks():
    print('\nКарты правил:')
    rule_cards_list = RuleCard.read_from_bd()
    # rule_cards_list.sort(key=lambda el: el.get_number())
    for i in rule_cards_list:
        print(i)
    print('\nКарты решений:')
    solution_cards_list = SolutionCard.read_from_bd()
    for i in solution_cards_list:
        print(i)
    history_cards_list = History_card.read_from_bd()
    print('\nКарты истории:')
    for i in history_cards_list:
        print(i)
    cards_tip_list = Card_tip.read_from_bd()
    print('\nКарта подсказки:')
    for i in cards_tip_list:
        print(i)
    cards_point_list = Card_point.read_from_bd()
    print('\nКарты судьбы:')
    for i in cards_point_list:
        print(i)
    choices_list = Choices.read_from_bd()
    print('\nКарты с вариантами ответа:')
    for i in choices_list:
        print(i)
    return [rule_cards_list, solution_cards_list, history_cards_list, cards_tip_list, cards_point_list, choices_list]


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
        init_from_bd_n_sort_by_decks()

