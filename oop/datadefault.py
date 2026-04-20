# implementing default values in data classes

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(0, 77))


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float =field(default_factory=price_func)
    # price: float =field(default=10.0)

b1 = Book()

print(b1.title)

b2 = Book("War and Peace", "Leo Tolstoy", 899)
print(b2.price)