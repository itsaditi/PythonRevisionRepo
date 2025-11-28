"""
Run with python3 condition.py
"""
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