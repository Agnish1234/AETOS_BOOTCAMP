'''x = 100

print(f"Value of x: {x}")
print(f"ID: {id(x)}")
print(f"Type: {type(x)}")

b = x
print(f"Value of b: {b}")

print(f"x is {x}, id(x) is {id(x)}")
print(f"b is {b}, id(b) is {id(b)}")

# You will see they have the SAME id. They are two names for the same object.'''


# Immutable Example
'''x = 10
print(f"Before operation: x = {x}, id(x) = {id(x)}")

x = x + 1  # We are "changing" x.
print(f"After operation:  x = {x}, id(x) = {id(x)}")

# Notice the ID changed! A new integer object was created.'''

# Mutable Example
'''my_list = [1, 2, 3]
print(f"Before append: my_list = {my_list}, id(my_list) = {id(my_list)}")

my_list.append(4)  # We are modifying the list.
print(f"After append:  my_list = {my_list}, id(my_list) = {id(my_list)}")

# Notice the ID stayed the same! The same list object was modified.'''

# The Problem:
list_1 = [1, 2, 3]  # Create a list object. Tag it `list_1`.
list_2 = list_1      # Create a new tag `list_2` and attach it to the SAME object.

list_1.append(4)     # Modify the object through the tag `list_1`.

print("list_1:", list_1) # Output: [1, 2, 3, 4]
print("list_2:", list_2) # Output: [1, 2, 3, 4]  <-- Surprise! list_2 is also changed.

