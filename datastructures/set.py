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