from datastructures.utils import print_data_types

"""
python3 variables.py
"""

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
