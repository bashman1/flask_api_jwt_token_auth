from api.models.book_model import BooksModel
from flask import make_response, jsonify, request

class BooksController():
    def __init__(self):
        self.books = []

    def add_book(self, args):

        book_model = BooksModel()

        book  = book_model.create_book(args)
        if not book or book is None:
            return make_response(jsonify({
                'message':'sorry! no books were found'
            }), 200)
        return make_response(jsonify({
            'message': 'successfully created book',
            'books': book
        }), 201)

    def get_books(self):
        book_model = BooksModel()

        books = book_model.get_books()
        if not books or len(books) < 1 or books is None:
            return make_response(jsonify({
                'message':'sorry! no books were found'
            }), 200)
        return make_response(jsonify({
            'message': 'success',
            'books': books
        }), 200)

    def get_book(self, book_id):
        book_model = BooksModel()

        book = book_model.get_book(book_id)
        if not book or book is None:
            return make_response(jsonify({
                'message':'sorry! book with Id not found'
            }), 200)
        return make_response(jsonify({
            'message': 'success',
            'books': book
        }), 200)