"""
python3 oop/inheritance.py
"""

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        # Initialize super class
        super().__init__(title, price)

        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, price, author, pages):

        # Initialize super class
        super().__init__(title, price)

        self.author = author
        self.pages = pages

class Magazine(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)

class Newspaper(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)


# Instaintiate class
book1 = Book("Brave New World", 29, "Aldous Huxley", 311)
np1 = Newspaper("NY Times", 6, "Daily", "New York Times Company")
m1 = Magazine("Scientific American", 5.99, "Monthly", "Springer Nature")

print(book1.author)
print(np1.publisher)
print(m1.period)