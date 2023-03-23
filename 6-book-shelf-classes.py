class Bookshelf:
    def __init__(self, capacity, books=[]):
        self.capacity = capacity
        self.books = []
        for book in books:
            self.addBook(book)
    
    def addBook(self, book):
        if len(self.books) == self.capacity:
            print(f"Bookshelf is full. Could not add '{book.title}'.")
            return
        if book not in self.books:  # (a)
            self.books.append(book)
    
    def __add__(self, other):
        if isinstance(other, Bookshelf):
            return [self, other]
        elif isinstance(other, Book):
            shelf2 = Bookshelf(self.capacity, list(self.books))
            shelf2.addBook(other)
            return shelf2

    def __str__(self):  # this gets called by print() and str()
        book_string = ', '.join([str(a) for a in self.books])
        space = self.capacity - len(self.books)
        return f'Books: {book_string}; This shelf can fit {space} more books'

    def __repr__(self):  # this gets called by repr() or when the object is displayed within an iterable/collection
        book_string = ', '.join([repr(a) for a in self.books])
        return f'Bookshelf({self.capacity}, [{book_string}])'

class Book:
    def __init__(self, title, author):
        self.title, self.author = title, author

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

    def __str__(self):
        return self.title + ', written by ' + self.author

fiction_shelf = Bookshelf(10)
nonfiction_shelf = Bookshelf(1)
frankenstein = Book('Frankenstein','Mary Shelley')
coraline = Book('Coraline','Neil Gaiman')
print(frankenstein) # (e)
adams = Book('John Adams','David McCullough')
hamilton = Book('Alexander Hamilton','Ron Chernow')
nonfiction_shelf.addBook(adams)
nonfiction_shelf += hamilton # (f)
fiction_shelf.addBook(frankenstein)
fiction_shelf += coraline
str(fiction_shelf) # (g)
