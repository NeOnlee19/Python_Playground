# TUPLES

# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "blue", "green")

single_item = (1, ) # PRZECINEK!
not_tuple = (42) # 42 w nawiasach i nic więcej

# Tuple without parentheses
coordinates = 10, 20

# Accessing items
print(point[0]) # 3
print(colors[-1]) # green
print(colors[0:3]) # ('red', 'blue', 'green')

x, y = coordinates
print(x) # 10
print(y) # 20

a, b, c, = 1, 2, 3
print(a, b, c) # 1, 2, 3

x, y = y, x
print(x, y) # Swaps values 20 10