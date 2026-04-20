# Using data classes to represent data objects
# Dataclass available in python verssion >= 3.7

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"{self.title} by {self.author}"


# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
print(b1.title)
print(b2.author)

# print the book itself - dataclasses implement __repr__
print(b1)

# comparing two dataclasses - they implement __eq__
print(b1 == b3)

# change some fields
b1.title = "Harry Potter"
b1.pages = 1000
print(b1.bookinfo())