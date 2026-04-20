"""
python3 oop/class_1.py
"""

# Basic class definition
class Book:
    # Class level attributes
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")


    # Initializer function like constructor in Java
    # Called when class is created, called before any other methods in class
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret atribute"

    # Instance method receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price
    
    def set_discount(self, amount):
        ## private to the method
        self._discount = amount

class Newspaper:
    def __init__(self, name):
        self.name = name
    

# Instance of class
book1 = Book("Hello world", "Aditi", "344", 50)
book2 = Book("The Housemaid", "Friedda", "250", 25.99)
newspaper1 = Newspaper("Newyork Times")

# Print the class and property
print(f"Book class book1: {book1}")
print(f"Book class book2: {book2}")
print(f"book1.title: {book1.title}, book2.title: {book2.title}")
print(f"book1.get_price(): {book1.get_price()}, book2.get_price(): {book2.get_price()}")
book1.set_discount(0.50)
print(f"Price after setting discount - \n" + 
    f"book1.get_price(): {book1.get_price()}," +
    f"book2.get_price(): {book2.get_price()}")


# Type function to inspect object type
print(f"type(book1): {type(book1)}")
print(f"type(newspaper1): {type(newspaper1)}")

# Compare two types instance
print(f"type(book1) == type(book2): {type(book1) == type(book2)}") # true
print(f"type(book1) == type(newspaper1): {type(book1) == type(newspaper1)}") # false

# isinstance to compare a specific instance to a known type
print(f"isinstance(book1, Book): {isinstance(book1, Book)}")
print(f"isinstance(book2, Book): {isinstance(book2, Book)}")
print(f"isinstance(newspaper1, Book): {isinstance(newspaper1, Book)}")

# In python, every object is a subclass of the built-in object class
print(f"isinstance(book1, object): {isinstance(book1, object)}")