import sqlite3


class Card:  # Карты с описанием игры(карты правил, Завершающие карты)
    def __init__(self, state, description):
        self.state = state  # Открыта или закрыта(прочитана или непрочитана)
        self.description = description  # Надпись на самой карте

    def __str__(self):
        return '\nstate: ' + str(self.state) + '\ndescription: ' + self.description

    def get_state(self):
        return self.state

    def get_description(self):
        return self.description


class Card_tip(Card):  # Карты подсказок
    def __init__(self, state, description, name):
        super().__init__(state, description)
        self.name = name  # Название карты на лицевой стороне

    def __str__(self):
        return super().__str__() + '\nname: ' + self.name

    def get_name(self):
        return self.name


class History_card(Card):  # Игровые карты с историей
    def __init__(self, state, description, prescription, scene, valid_date, choices):
        super().__init__(state, description)
        self.prescription = prescription  # Давность действия
        self.scene = scene  # Место действия
        self.valid_date = valid_date  # Дата действия
        self.choices = choices  # Массив с вариантами выбора

    def __str__(self):
        return super().__str__() + '\nprescription: ' + self.prescription + '\nscene: ' + self.scene + '\nvalid_date: ' + self.valid_date + '\nchoices:' + self.choices

    def get_prescription(self):
        return self.prescription

    def get_scene(self):
        return self.scene

    def get_valid_date(self):
        return self.valid_date

    def get_choices(self):
        return self.choices


class Card_point:
    def __init__(self, choices, score):
        self.choices = choices  # Вариант ответа
        self.score = score  # Количество очков

    def __str__(self):
        return '\nchoices: ' + self.choices + '\nscore: ' + str(self.score)

    def get_choices(self):
        return self.choices

    def get_score(self):
        return self.score


def create_db_to_cards():
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS cards(state INTEGER, description TEXT)')
    cur.close()
    con.close()


def create_db_to_cards_tip():
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS cards_tip(state INTEGER, description TEXT, name TEXT)')
    cur.close()
    con.close()


def create_db_to_history_cards():
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS history_cards(state INTEGER,'
                'description TEXT,'
                'prescription TEXT,'
                'scene TEXT,'
                'date TEXT,'
                'choices TEXT)')
    # todo: text в choices заменить на массив
    cur.close()
    con.close()


def create_db_to_cards_point():
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS cards_point(choices TEXT, score INTEGER)')
    cur.close()
    con.close()


def write_to_db_to_cards(card):
    list_to_add = []
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    # print('state [True/False]: ', end='')
    state = card.get_state()
    list_to_add.append(state)
    # print('description [Надпись на самой карте]: ', end='')
    description = card.get_description()
    list_to_add.append(description)
    cur.execute('INSERT INTO cards VALUES(?, ?)', list_to_add)
    con.commit()
    cur.close()
    con.close()


def write_to_db_to_cards_tip(card_tip):
    list_to_add = []
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    # print('state [True/False]: ', end='')
    state = card_tip.get_state()
    list_to_add.append(state)
    # print('description [Надпись на самой карте]: ', end='')
    description = card_tip.get_description()
    list_to_add.append(description)
    # print('name [Название карты на лицевой стороне]: ', end='')
    name = card_tip.get_name()
    list_to_add.append(name)
    cur.execute('INSERT INTO cards_tip VALUES(?, ?, ?)', list_to_add)
    con.commit()
    cur.close()
    con.close()


def write_to_db_to_history_cards(history_card):
    list_to_add = []
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    # print('state [True/False]: ', end='')
    state = history_card.get_state()
    list_to_add.append(state)
    # print('description [Надпись на самой карте]: ', end='')
    description = history_card.get_description()
    list_to_add.append(description)
    # print('prescription [Давность действия]: ', end='')
    prescription = history_card.get_prescription()
    list_to_add.append(prescription)
    # print('scene [Место действия]: ', end='')
    scene = history_card.get_scene()
    list_to_add.append(scene)
    # print('date [Дата действия]: ', end='')
    date = history_card.get_valid_date()
    list_to_add.append(date)
    # print('choices [Массив с вариантами выбора]: ', end='')
    choices = history_card.get_choices()
    list_to_add.append(choices)
    cur.execute('INSERT INTO history_cards VALUES(?, ?, ?, ?, ?, ?)', list_to_add)
    con.commit()
    cur.close()
    con.close()


def write_to_db_to_cards_point(card_point):
    list_to_add = []
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    # print('choices [Вариант ответа]: ', end='')
    choices = card_point.get_choices()
    list_to_add.append(choices)
    # print('score [Количество очков]: ', end='')
    score = card_point.get_score()
    list_to_add.append(score)
    cur.execute('INSERT INTO cards_point VALUES(?, ?)', list_to_add)
    con.commit()
    cur.close()
    con.close()


def read_from_bd_cards():  # Чтение экземпляров класса Card из базы данных
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM cards')
    cardlist_in_db = cur.fetchall()
    cards_list = []
    for card in cardlist_in_db:
        state = card[0]
        description = card[1]
        cards_list.append(Card(state, description))
    cur.close()
    con.close()
    return cards_list


def read_from_bd_cards_tip():  # Чтение экземпляров класса Card_tip из базы данных
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM cards_tip')
    cardlist_in_db = cur.fetchall()
    cards_tip_list = []
    for card in cardlist_in_db:
        state = card[0]
        description = card[1]
        name = card[2]
        cards_tip_list.append(Card_tip(state, description, name))
    cur.close()
    con.close()
    return cards_tip_list


def read_from_bd_history_cards():  # Чтение экземпляров класса History_card из базы данных
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM history_cards')
    cardlist_in_db = cur.fetchall()
    history_cards_list = []
    for card in cardlist_in_db:
        state = card[0]
        description = card[1]
        prescription = card[2]
        scene = card[3]
        date = card[4]
        choices = card[5]
        history_cards_list.append(History_card(state, description, prescription, scene, date, choices))
    cur.close()
    con.close()
    return history_cards_list


def read_from_bd_cards_point():  # Чтение экземпляров класса Card_point из базы данных
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM cards_point')
    cardlist_in_db = cur.fetchall()
    cards_point_list = []
    for card in cardlist_in_db:
        choices = card[0]
        score = card[1]
        cards_point_list.append(Card_point(choices, score))
    cur.close()
    con.close()
    return cards_point_list


if __name__=="__main__":
    create_db_to_cards()
    create_db_to_cards_tip()
    create_db_to_history_cards()
    create_db_to_cards_point()
    print('Хотите ввести новое значение?[0/1]:', end=' ')
    ans = int(input())
    if ans == 1:
        choice = True
    else:
        choice = False
    while choice:
        print('Какого типа карту хотите добавить?[Card/Card_tip/History_card/Card_point]', end=' ')
        ans = input()
        if ans == 'Card':
            print('state: ', end='')
            state = input()
            print('description: ', end='')
            description = input()
            card = Card(state, description)
            write_to_db_to_cards(card)
        elif ans == 'Card_tip':
            print('state: ', end='')
            state = input()
            print('description: ', end='')
            description = input()
            print('name: ', end='')
            name = input()
            card_tip = Card_tip(state, description, name)
            write_to_db_to_cards_tip(card_tip)
        elif ans == 'History_card':
            print('state: ', end='')
            state = input()
            print('description: ', end='')
            description = input()
            print('prescription: ', end='')
            prescription = input()
            print('scene: ', end='')
            scene = input()
            print('date: ', end='')
            date = input()
            print('choices: ', end='')
            choices = input()
            history_card = History_card(state, description, prescription, scene, date, choices)
            write_to_db_to_history_cards(history_card)
        elif ans == 'Card_point':
            print('choices: ', end='')
            choices = input()
            print('score: ', end='')
            score = input()
            card_point = Card_point(choices, score)
            write_to_db_to_cards_point(card_point)
    print('Хотите прочитать всю базу данных?[0/1]:', end=' ')
    ans = int(input())
    if ans == 1:
        cards_list = read_from_bd_cards()
        for i in cards_list:
            print(i)
        cards_tip_list = read_from_bd_cards_tip()
        for i in cards_tip_list:
            print(i)
        history_cards_list = read_from_bd_history_cards()
        for i in history_cards_list:
            print(i)
        cards_point_list = read_from_bd_cards_point()
        for i in cards_point_list:
            print(i)
