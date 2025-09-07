class Book:
    def __init__(self,title: str,author: str):
        self.title = title
        self.author = author 
class EBook(Book):
    def __init__(self, file_size: int)
        self.file_size = file_size
class PrintBook(Book):
    def __init__(self, page_count: int)
        self.page_count = page_count
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book: Book ):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book, EBook, or PrintBook instances can be added.")
    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)