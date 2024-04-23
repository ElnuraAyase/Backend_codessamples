from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
]

# Create
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = {"id": len(books) + 1, "title": data["title"], "author": data["author"]}
    books.append(new_book)
    return jsonify(new_book), 201

# Read
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)


