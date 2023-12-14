import sqlite3

connection = sqlite3.connect("bookstore.db")
def get_borrowers(id=None):
    cursor = connection.cursor()

    if id is None:
        cursor.execute("SELECT * FROM borrowers")
    else:
        cursor.execute(f"SELECT * FROM borrowers WHERE borrower_id={id}")

    rows = cursor.fetchall()
    borrowers = [{'borrower_id': row[0], 'name': row[1], 'email': row[2], 'cid': row[3]} for row in rows]

    return borrowers
def get_items(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select * from books")
    else:
        rows = cursor.execute(f"select * from books where book_id={id}")
    rows = cursor.fetchall()
    rows = list(rows)
    books = [{'book_id': row[0], 'title': row[1], 'author': row[2], 'quantity': row[3]} for row in rows]
    return books


def add_item(title,author,quantity):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)", (title,author,quantity))
    connection.commit()

def add_bor(name,email,bid):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO borrowers (name, email, cid) VALUES (?, ?, ?)", (name,email,bid))
    connection.commit()

def delete_item(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from books where book_id={id}")
    connection.commit()
def delete_bor(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from borrowers where borrower_id={id}")
    connection.commit()
def update_bor(id, name, email, bid):
    cursor = connection.cursor()
    cursor.execute(f"update borrowers set cid={cid},name='{name}',email='{email}' where borrower_id={id}")
    connection.commit()    
def update_item(id,title,author,quantity):
    cursor = connection.cursor()
    cursor.execute(f"update books set title='{title}',author='{author}',quantity='{quantity}' where book_id={id}")
    connection.commit()
def search_book(title):
    cursor = connection.cursor()
    cursor.execute(f"SELECT borrowers.borrower_id, borrowers.name, borrowers.email,books.title,borrowers.cid FROM books JOIN borrowers ON books.book_id = borrowers.cid WHERE books.title = '{title}'")
    connection.commit()
    results = cursor.fetchall()
    return results
   
