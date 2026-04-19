"""
python3 class_2.py
"""

# Basic class definition
class Book:
    # Class level attributes
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # double underscore properties are hidden from other class
    __booklist = None

    # Initializer function like constructor in Java
    # Called when class is created, called before any other methods in class
    def __init__(self, title, booktype):
        self.title = title

        if (not booktype in self.BOOK_TYPES):
            raise ValueError(f"{booktype} is an invalid booktype")
        else:
            self.booktype = booktype

    # Class Methods
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    
    # Static methos for Singleton classes
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        
        return Book.__booklist


# Access Class Attributes
print("Book types:", Book.get_book_types())

# Instance of class
book1 = Book("Hello world", "HARDCOVER")
book2 = Book("The Housemaid", "HARDCOVER")
# book2 = Book("The Housemaid", "COMICBOOK") # Throws error

# Use static method to access a singleton object
books = Book.getbooklist()
books.append(book1)
books.append(book2)
print(books)