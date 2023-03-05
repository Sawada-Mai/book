import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE book
              (id INTEGER primary key, title TEXT, purpose TEXT, point INTEGER, thoughts TEXT,memo TEXT)''')

connection.commit()
connection.close()