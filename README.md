
# Useful commands

### Command to create virtual env
```python
python3 -m venv .venv
```

### Command to run virtual env
```python
source venv/bin/activate
```

# Basic

## Variables -
See [variables.py](./variables.py)

```python
# Hello world with variable
msg: str = "Hello world"
print(f"{msg}")

# f string using variables in string
first_name: str = "albert"
last_name: str = "einstein"
full_name = f"{first_name} {last_name}"
print_data_types(full_name)

# Integer
age:int = 1
print_data_types(age)

# String
first_name: str = "albert"
last_name: str = "einstein"

# Float
num: float = 3.14
print_data_types(num)

signed_num = -3
print_data_types(signed_num)

# Bool
isAvailable: bool = False
print_data_types(isAvailable)

# Complex - Numbers with a real and imaginary part
complex_num: complex = 2 + 3j
print_data_types(complex_num)

```

## Math

See [math.py](./math.py)

```python
# Division returns a float
div = 2 / 3 
print(round(div, 2))

# Floor division returns int, 
# discarding fractional part
floor_division = 5 // 3

# Modulo returns remainder of division
modulo = 2 % 3

# Exponentiation
square = 3 ** 2
cube = 2 ** 3

print(floor_division)
print(modulo)
print(square)
print(cube)

"""
Built-in math operations
"""
nums = [5, 10, 2, 25, 8, 12]
print(min(nums))
print(max(nums))

print(abs(-3.14))
print(round(div, 2))
print(pow(10, 2))

```

## Conditions
See [conditions.py](./conditions.py)

```python
print(1 == 2) # False
print(1 != 2, 1 is not 2) # True True

bikes = ['trek', 'mountain', 'road']
print('trek' in bikes)  # True
print('something else' in bikes)  # False
print('road' not in bikes) # False

"""
If-elif-else
"""
age = 9
if age > 70:
    print("You are too old to vote")
elif age >= 18:
    print("You can vote!")
elif 10 >= age > 7:
    print(f"You need to wait for {18 - age} more years years")
else:
    print("You cannot vote")

"""
Match-case
"""
status_code = 200

match status_code:
    case 200:
        print("OK- Request successful")
    case 404:
        print("Not found - Resources not found")
    case 500:
        print("Internal server error")
    case _:
        print("Unknown error")

```

## Datastructures

### List - Mutable - Stack
See [list.py](./datastructures/list.py)

```python
"""
List is mutable
"""
list_var: list = [0, 1, 2, 3]
print_data_types(list_var)

first_num = list_var[0]
print_data_types(f"first_num - {first_num}")
last_num = list_var[1]
print_data_types(f"last_num - {last_num}")

nested_list: list[list[str]] = [["hello", "world"], "b", 'c']
print_data_types(f"nested_list - {nested_list}")

# Adding to list
list_var.append(4)
list_var.append(5)

# Range
print("Range - range(0, n - 1)")
for x in range(1, 10):
    print(x)

# Looping through list
print("Looping through the list")
for index in range(0, len(list_var)):
    print(list_var[index])

# Making numerical lists
squares: list = []
for index in range(1, 11):
    squares.append(index**2)

print_data_types(f"sqaures - {squares}")

# List comprehension
squares = [x**2 for x in range(1, 11)]

# Slicing a list [start:end:step]
# element at end index is not included
first_two = list_var[:2]
print(
    f"list_var - {list_var}" +
    f" first_two - {first_two}"
)

start_from_two = list_var[2:]
print(
    f"list_var - {list_var}" +
    f" start_from_two - {start_from_two}"
)


start_end = list_var[1:4]
print(
    f"list_var - {list_var}" +
    f" start_end = list_var[1:4] - {start_end}"
)

with_step = list_var[1:4:2]
print(
    f"list_var - {list_var}" +
    f" with_step = list_var[1:4:2] - {with_step}"
)

# Reverse list
reverse_list = list_var[::-1]
print(
    f"list_var - {list_var}" +
    f" reverse_list = list_var[::-1] - {reverse_list}"
)

reverse_list_2 = list_var[::-2]
print(
    f"list_var - {list_var}" +
    f" reverse_list_2 = list_var[::-2] - {reverse_list_2}"
)

msg = "Hello world"
reverse_string = msg[::-1]
print(
    f"list_var - {list_var}" +
    f" reverse_string = msg[::-1] - {reverse_string}"
)

# Copying a list
list_var_copy = list_var[:]
print(
    f"list_var - {list_var}" +
    f" list_var_copy = list_var[:] - {list_var_copy}"
)

```

### Tuple
See [tuple.py](./datastructures/tuple.py)

```python
dimensions: tuple = (1, 2, 3)
string_tuple: tuple = ('a', 'b', "hello")
print_data_types(dimensions)
print_data_types(string_tuple)

# Cannot append or add to tuple,
# it can be concatenated
concatenated_tuple = dimensions + string_tuple
print(concatenated_tuple)
print(len(dimensions))

for x in range(0, len(concatenated_tuple)):
    print(concatenated_tuple[x])

print(concatenated_tuple[3:])
```

### Dictionary
See [dictionary.py](./datastructures/dictionary.py)

```python
alien: dict = {
    'color': 'green',
    'points': 5,
    'texture': 'weird'
}

print(f"The alien's color is {alien['color']}")

alien['new_key'] = 0

# Looping through all items
for key, value in alien.items():
    print(f"Key is {key} and value is {value}")

# Looping through all keys
for key in alien.keys():
    print(f"Key is {key}")

# Looping through all values
for value in alien.values():
    print(f"Value is {value}")
```

### Stack

[stack.py](./datastructures/stack.py)

#### Using Doubly Ended Queue

```python
from collections import deque

## Using Double ended queue
stack = deque()

# Enqueue elements into the queue
stack.append('Task 1')
stack.append('Task 2')
stack.append('Task 3')
stack.append('Task 4')

print(stack)

while len(stack) != 0:
    print("Dequeued element", stack.pop())

```

#### Using List

```python
## Using List
list_queue = []

list_queue.append('Task 1')
list_queue.append('Task 2')
list_queue.append('Task 3')
list_queue.append('Task 4')

print(list_queue)

while len(list_queue) != 0:
    print("Dequeued element", list_queue.pop())

```

### Queue

[queue.py](./datastructures/queue.py)

#### Using Doubly Ended Queue

```python

from collections import deque

## Using Double ended queue
queue = deque()

# Enqueue elements into the queue
queue.append('Task 1')
queue.append('Task 2')
queue.append('Task 3')
queue.append('Task 4')

print(queue)

while len(queue) != 0:
    print("Dequeued element", queue.popleft())

```

#### List

```python

## Using List
list_queue = []

list_queue.append('Task 1')
list_queue.append('Task 2')
list_queue.append('Task 3')
list_queue.append('Task 4')

print(list_queue)

while len(list_queue) != 0:
    print("Dequeued element", list_queue.pop(0))

```

### Set - unordered
See [set.py](./datastructures/set.py)

```python
new_set = {"apple", "banana", "cherry", "apple"}
print(new_set) # {'cherry', 'banana', 'apple'}

num_set = set()
num_set.add(1)
num_set.add(9)
num_set.add(6)
num_set.add(3)
num_set.add(1)

print(num_set) # {1, 3, 9, 6}

## Convert list to set

num_list = [99, 7, 5, 8, 99, 0, 2, 33, 4, 4, 5, 5]
num_set_2 = set(num_list)
print(num_set_2) # {0, 33, 2, 99, 4, 5, 7, 8}
```


# OOP Refresher

## Class

* A class is a collection of objects. 
* Classes are blueprints for creating objects. 
* A class defines a set of attributes and methods that the created objects (instances) can have

## Objects

* An Object is an instance of a Class. 
* It represents a specific implementation of the class and holds its own data. 
* An object consists of:

  * State: It is represented by the attributes and reflects the properties of an object.
  * Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
  * Identity: It gives a unique name to an object and enables one object to interact with other objects.


| Term | Definition | 
|---|---|
| Class | Collection of objects, A blueprint for creating objects of particular type. A class defines a set of attributes and methods that the created objects (instances) can have |
| Methods | Regular functions that are part of a class |
| Attributes | Variables that hold data that are part of a class |
| Object | Specific instance of a class |
| Inheritance | Means by which class can inherit capabilities from another |
| Composition | Means of building complex obj out of other objects |

## Four Pillars of OOP

### Inheritance

Inheritance allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse.

### Polymorphism

* Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different types to be treated as objects of a common super type. 
* This enables a single interface to work with various data types, making code easier to write and maintain.

#### Types of Polymorphism

* Compile-time Polymorphism (Static Polymorphism)
  * Method Overloading: Multiple methods in the same class can have the same name but different parameters. The method to be executed is determined at compile time based on the method signature.
* Runtime Polymorphism (Dynamic Polymorphism)
  * Method Overriding: A subclass can provide a specific implementation of a method that is already defined in its superclass. The method to be executed is determined at runtime, allowing for more flexible code.

### Encapsulation

* Encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions. 
* A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

### Abstraction

* Abstraction hides the internal implementation details while exposing only the necessary functionality. 
* It helps focus on "what to do" rather than "how to do it."

# Naming conventions 

## Underscores in Naming Conventions

### Single Leading Underscore (`_name`)

This is a naming convention to indicate that a variable, function, or method is intended for internal use (non-public) within a module or class. Python does not strictly enforce this, but it serves as a hint to other programmers and prevents the name from being imported by a wildcard import (from module import *).

### Single Trailing Underscore (`name_`): 

This convention is used to avoid naming conflicts with Python keywords or built-in names. For example, you can use class_ as a variable name instead of class, which is a reserved keyword.

### Double Leading Underscore (`__name`): 
When used within a class definition, this triggers a language feature called name mangling. The Python interpreter automatically changes the name to `_ClassName__name` to help prevent accidental overriding of attributes in subclasses. It does not create a truly "private" variable, as the mangled name can still be accessed directly.


### Double Leading and Trailing Underscore :

These are special methods, often referred to as "dunder" (double underscore) or "magic" methods, that have specific functionality defined by the Python language. Examples include `__init__`, `__str__`, and `__len__`. You should avoid using this naming scheme for your own attributes to prevent conflicts with future Python language features



# Useful in-built functions

## hasattr
checks whether an object has a specified named attribute or method and returns a boolean result. 

```python
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.price = price

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price
    
    def set_discount(self, amount):
        ## private to the method
        self._discount = amount
```