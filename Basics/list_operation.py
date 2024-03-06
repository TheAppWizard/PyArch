# Append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Extend
my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Insert
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]

# Remove
my_list = [1, 2, 3, 4]
my_list.remove(4) # Exact Remove
print(my_list)  # Output: [1, 2, 4]

# Pop
my_list = [1, 2, 3]
popped_item = my_list.pop(1)
print(popped_item)  # Output: 2 Position Remove
print(my_list)      # Output: [1, 3]

# Index
my_list = [1, 2, 3, 4, 3]
print(my_list.index(3))  # Output: 2 Position Index

# Count
my_list = [1, 2, 3, 4, 3]
print(my_list.count(3))  # Output: 2


# Sort 
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]


# Reverse
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

# Clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []

