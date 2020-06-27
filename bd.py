import sqlite3


def create_db_to_card():
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS cards(state INTEGER, description TEXT)')
    cur.close()
    con.close()


def create_db_to_card_tip():
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS cards_tip(state INTEGER, description TEXT, name TEXT)')
    cur.close()
    con.close()


def create_db_to_history_card():
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


def create_db_to_card_point():
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS cards_point(choices TEXT, score INTEGER)')
    cur.close()
    con.close()


def write_to_db_to_card():
    list_to_add = []
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    print('state: ', end='')
    state = input()
    list_to_add.append(state)
    print('description: ', end='')
    description = input()
    list_to_add.append(description)
    cur.execute('INSERT INTO cards VALUES(?, ?)', list_to_add)
    con.commit()
    cur.close()
    con.close()


def write_to_db_to_card_tip():
    list_to_add = []
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    print('state: ', end='')
    state = input()
    list_to_add.append(state)
    print('description: ', end='')
    description = input()
    list_to_add.append(description)
    print('name: ', end='')
    name = input()
    list_to_add.append(name)
    cur.execute('INSERT INTO cards_tip VALUES(?, ?, ?)', list_to_add)
    con.commit()
    cur.close()
    con.close()


def write_to_db_to_history_card():
    list_to_add = []
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    print('state: ', end='')
    state = input()
    list_to_add.append(state)
    print('description: ', end='')
    description = input()
    list_to_add.append(description)
    print('prescription: ', end='')
    prescription = input()
    list_to_add.append(prescription)
    print('scene: ', end='')
    scene = input()
    list_to_add.append(scene)
    print('date: ', end='')
    date = input()
    list_to_add.append(date)
    print('choices: ', end='')
    choices = input()
    list_to_add.append(choices)
    cur.execute('INSERT INTO history_cards VALUES(?, ?, ?, ?, ?, ?)', list_to_add)
    con.commit()
    cur.close()
    con.close()


def write_to_db_to_card_point():
    list_to_add = []
    con = sqlite3.connect('./game_base.db')
    cur = con.cursor()
    print('choices: ', end='')
    choices = input()
    list_to_add.append(choices)
    print('score: ', end='')
    score = input()
    list_to_add.append(score)
    cur.execute('INSERT INTO cards_point VALUES(?, ?)', list_to_add)
    con.commit()
    cur.close()
    con.close()


create_db_to_card()
create_db_to_card_tip()
create_db_to_history_card()
create_db_to_card_point()
print('Хотите ввести новое значение?[0/1]', end=' ')
ans = int(input())
if ans == 1:
    choice = True
else:
    choice = False
while choice:
    print('Какого типа карту хотите добавить?[Card/Card_tip/History_card/Card_point]', end=' ')
    ans = input()
    if ans == 'Card':
        write_to_db_to_card()
    elif ans == 'Card_tip':
        write_to_db_to_card_tip()
    elif ans == 'History_card':
        write_to_db_to_history_card()
    elif ans == 'Card_point':
        write_to_db_to_card_point()
    print('Хотите ввести новое значение?[0/1]', end=' ')
    ans = int(input())
    if ans == 1:
        choice = True
    else:
        choice = False

