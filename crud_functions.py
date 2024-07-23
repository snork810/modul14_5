import sqlite3
connection = sqlite3.connect('Products.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
''')
texts = [
        'Набор из 20ти пар уютных теплых носки с разными принтами!',
        'Самые мягкие и удобные футболки с сказочными принтами!',
        'Модные джинсы из лучшей ткани!',
        'Теплая удобная и стильная куртка для прохладной осени!'
    ]
products = ['Носки','Футболка','Джинсы','Куртка']
prices = ['100', '200', '300', '400']
# for prod, text, pr in zip(products, texts, prices):
#     cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)', (prod, text, pr))

def get_all_product():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT title FROM Products')
    title_list = cursor.fetchall()
    cursor.execute('SELECT description FROM Products')
    descriptions_list = cursor.fetchall()
    cursor.execute('SELECT price FROM Products')
    prices_list = cursor.fetchall()
    return [title_list, descriptions_list, prices_list]



connection.commit() #Сохраняет состояние бд перед закрытием
connection.close()

connection = sqlite3.connect('HW_bot_Users.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS HW_bot_Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
''')
def is_included(username):
    connection = sqlite3.connect('HW_bot_Users.db')
    cursor = connection.cursor()
    s = cursor.execute('SELECT username FROM HW_bot_Users').fetchall()
    connection.commit()
    return (username,) in s

def add_user(username, email, age):
    connection = sqlite3.connect('HW_bot_Users.db')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO HW_bot_Users (username, email, age, balance) VALUES("{username}", "{email}", "{age}", 1000)')
    connection.commit()

connection.commit() #Сохраняет состояние бд перед закрытием
connection.close()