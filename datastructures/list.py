"""
Run with command in root dir -
python -m datastructures.list
"""


from datastructures.utils import *
print("***************** LIST *****************")

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

