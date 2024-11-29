import random
import sqlite3


def initiate_db():
    connection = sqlite3.connect('bot_database.db')
    cursor = connection.cursor()
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')

    for i in range(1, 5):
        cursor.execute("INSERT INTO Products(id, title, description, price) VALUES(?, ?, ?, ?)",
                       (i, f'Продукт {i}', f'Описание {i}', f'{i * 100}'))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('bot_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products
