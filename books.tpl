<!-- books.tpl -->
<!DOCTYPE html>
<html>
<head>
    <title>Books</title>
</head>
<body>
    <h1>Books</h1>
    <ul>
        % for book in books:
            <li>
                <a href="/books/{{ book['id'] }}">{{ book['title'] }}</a>
            </li>
        % end
    </ul>
    <a href="/books/add">Add a Book</a>
</body>
</html>
