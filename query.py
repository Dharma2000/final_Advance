import sqlite3

connection = sqlite3.connect("bookstore.db")

cursor = connection.cursor()

books = cursor.execute("select * from books")

print(books.fetchall())

borrowers = cursor.execute("select * from borrowers")

print(borrowers.fetchall())
