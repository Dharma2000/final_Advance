import sqlite3

connection = sqlite3.connect("bookstore.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table books")
    cursor.execute("drop table borrowers")
except:
    pass

cursor.execute("create table books(book_id integer primary key, title text,author text,quantity integer)")
cursor.execute("create table borrowers(borrower_id integer primary key,name text,email text,cid integer,FOREIGN KEY(cid) REFERENCES books(book_id))")
cursor.execute("""INSERT INTO books VALUES(1,'python','sunny',12)""")
cursor.execute("""INSERT INTO borrowers VALUES(1,"potter",'abc@gmail.com',1)""")
connection.commit()
connection.close()
