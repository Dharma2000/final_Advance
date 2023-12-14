<!-- book_details.tpl -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ book['title'] }} Details</title>
</head>
<body>
    <h1>{{ book['title'] }} Details</h1>
    <p>Title: {{ book['title'] }}</p>
    <p>Author: {{ book['author'] }}</p>
    <p>Genre: {{ book['genre'] }}</p>
    <!-- Add ratings or any other details you want to display -->
    <a href="/books/{{ book['id'] }}/update">Update Book</a>
    <a href="/books/{{ book['id'] }}/delete">Delete Book</a>
    <a href="/books">Back to Books</a>
</body>
</html>
