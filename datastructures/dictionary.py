"""
Run with command in root dir -
python -m datastructures.dictionary
"""

print("***************** DICTIONARY *****************")

"""
Dictionaries
"""
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