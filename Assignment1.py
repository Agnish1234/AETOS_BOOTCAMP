def modify_data(a, b):
    a = a * 2
    b.append('world')
    print(f"Inside function: a = {a}, id(a) = {id(a)}")
    print(f"Inside function: b = {b}, id(b) = {id(b)}")

x = 10      # Immutable integer
y = ['hello'] # Mutable list

print(f"Before function: x = {x}, id(x) = {id(x)}")
print(f"Before function: y = {y}, id(y) = {id(y)}")

modify_data(x, y)

print(f"After function:  x = {x}, id(x) = {id(x)}")
print(f"After function:  y = {y}, id(y) = {id(y)}")