books = []
class BooksModel():
    def __init__(self):
        self.books = books

    def create_book(self, args):
        try:
            book = dict(
                book_id= len(self.books)+1,
                title=args['title'],
                author=args['author'],
                issbn=args['issbn'],
                description=args['description']
            )

            books.append(book)

            return book

        except Exception as ex:
            return ex

    def get_books(self):
        return  self.books

    def get_book(self, book_id):
        for book in books:
            if book['book_id'] == book_id:
                return book

        return None