# book_store.py

from bottle import route, post, run, template, redirect, request
import database

# Initialize the database
database.initialize_database()

@route("/")
def get_index():
    redirect("/books")

@route("/books")
def get_books():
    books = database.get_all_books()
    return template("books.tpl", books=books)

@route("/books/add")
def get_add_book():
    return template("add_book.tpl")

@post("/books/add")
def post_add_book():
    title = request.forms.get("title")
    author = request.forms.get("author")
    genre = request.forms.get("genre")
    database.add_book(title, author, genre)
    redirect("/books")

@route("/books/<book_id>")
def get_book_details(book_id):
    book = database.get_book_details(book_id)
    return template("book_details.tpl", book=book)

@route("/books/<book_id>/update")
def get_update_book(book_id):
    book = database.get_book_details(book_id)
    return template("update_book.tpl", book=book)

@post("/books/<book_id>/update")
def post_update_book(book_id):
    title = request.forms.get("title")
    author = request.forms.get("author")
    genre = request.forms.get("genre")
    database.update_book(book_id, title, author, genre)
    redirect("/books")

@route("/books/<book_id>/delete")
def get_delete_book(book_id):
    database.delete_book(book_id)
    redirect("/books")

run(host='localhost', port=8080)


