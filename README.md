
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
