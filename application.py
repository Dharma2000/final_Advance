from bottle import bottle,template, redirect, request,static_file
import database
app = bottle()
@app.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='')
@app.route("/")
def get_list():
    rows = database.get_items()
    n=database.get_borrowers()
    return template("list", books=rows,borrowers=n)
@app.post('/search')
def search():
    search_query = request.forms.get('search_query', '')
    results=database.search_book(search_query)
    return template('search_results', results=results, search_query=search_query)
@app.route("/add")
def get_add():
    return template("add_item.tpl")

@app.post("/add")
def post_add():
    title = request.forms.get("title")
    author=request.forms.get("author")
    quantity=request.forms.get("quantity")
    database.add_item(title,author,quantity)
    redirect("/")
@app.route("/update/<id>")
def get_update(id):
    rows = database.get_items(id)
    if len(rows) != 1:
        redirect("/")
    title = rows[0]['title']
    author = rows[0]['author']
    quantity = rows[0]['quantity']

    return template("update_item.tpl", id=id,title=title,author=author,quantity=quantity)

@app.post("/update")
def post_update():
    title = request.forms.get("title")
    author=request.forms.get("author")
    quantity=request.forms.get("quantity")
    id = request.forms.get("id")
    database.update_item(id, title,author,quantity)
    redirect("/")
@app.route("/delete/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect("/")
@app.route("/addb")
def get_addb():
    return template("add_bor.tpl")
@app.post("/addb")
def post_add():
   
    name = request.forms.get("name")
    email=request.forms.get("email")
    bid=request.forms.get("bid")
    database.add_bor(name,email,bid)
    redirect("/")

@app.route("/deletebor/<id>")
def get_delete(id):
    database.delete_bor(id)
    redirect("/")
@app.route("/updateb/<id>")
def get_updatebor(id):
    b = database.get_borrowers(id)
    if len(b) != 1:
        redirect("/list")
    name = b[0]['name']
    email = b[0]['email']
    bid = b[0]['bid']

    return template("update_bor.tpl", id=id,name=name,email=email,bid=bid)

@app.post("/updateb")
def post_updatebor():
    id = request.forms.get("id")
    id=int(id)
    name = request.forms.get("name")
    email=request.forms.get("email")
    bid=request.forms.get("bid")
    bid=int(bid)
    database.update_bor(id,name,email,bid)
    redirect("/")
if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)