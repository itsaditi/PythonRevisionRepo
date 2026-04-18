# Basic class definition
class Book:
    # Initializer function like constructor in Java
    # Called when class is created, called before any other methods in class
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret atribute"

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price
    
    def set_discount(self, amount):
        ## private to the method
        self._discount = amount


# Instance of class
book1 = Book("Hello world", "Aditi", "344", 50)
book2 = Book("The Housemaid", "Friedda", "250", 25.99)

# Print the class and property
print(book1)
print(book2)
print(book1.title, book2.title)
print(book1.get_price(), book2.get_price())
book1.set_discount(0.50)
print(book1.get_price(), book2.get_price())
