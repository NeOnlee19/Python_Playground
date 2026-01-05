# SETS

# Empty set
empty_set = set() # NIE {}

# Sets with values
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "orange", "banana"])

# From a list
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)
print(unique_scores) # {90, 92, 85}

# Adding items
fruits.add("cherry")
print(fruits) # {'apple', 'orange', 'cherry', 'banana'}

# Removing items
fruits.remove("cherry") # Possible error
fruits.discard("orange") # No error
print(fruits) # {'apple', 'banana'}

# Checking if exist
if "apple" in fruits:
    print("apple found") # True

