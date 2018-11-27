from flask import request, Blueprint
from api.controllers.books_controller import BooksController

books_bt = Blueprint('books', __name__)
books_controller = BooksController()

@books_bt.route('/books')
def get_books():
    return books_controller.get_books()

@books_bt.route('/books/<int:bookId>')
def get_book(bookId):
    return books_controller.get_book(bookId)

@books_bt.route('/books', methods=['POST'])
def add_books():
    data = request.get_json()
    return books_controller.add_book(data)
