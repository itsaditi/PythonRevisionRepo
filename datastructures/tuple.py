"""
Run with command in root dir -
python -m datastructures.tuple
"""

from datastructures.utils import *

"""
Tuples - items in tuples cannot be modified
Tuples are Immutable
"""
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
