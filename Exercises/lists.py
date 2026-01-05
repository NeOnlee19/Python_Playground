# LISTS

# Empty List
list = []

# List with items
fruits = ['apple', 'banana', 'orange']
numbers = [3, 5, 1, 4, 2, 3]
mixed = ["hello", 42, True, 3.14]

# Accessing items
print(fruits[0]) # apple
print(fruits[-1]) # orange
print(fruits[0:3]) # ['apple', 'banana', 'orange']
print(fruits[1:]) # ['banana', 'orange']

# Changing lists
fruits[0] = "mango"
print(fruits[0]) # mango

# Adding items
fruits.append("grape")
fruits.insert(1, "kiwi")
print(fruits) # ['mango', 'kiwi', 'banana', 'orange', 'grape']

# Removing items
fruits.remove("banana")
last = fruits.pop()
del fruits[0]
print(fruits) # ['kiwi', 'orange']
print(last) # grape

# List methods
print(len(numbers)) # 6 (długość listy)
print(numbers.count(3)) # 2 (liczba trójek)
print(numbers.index(4)) # 3 (indeks czwórki)

# Sorting
numbers.sort()
print(numbers) # [1, 2, 3, 3, 4, 5]
numbers.reverse()
print(numbers) # [5, 4, 3, 3, 2, 1]

# Copy
new_numbers = numbers.copy() # tworzy kopię

# Checking lists
if "kiwi" in fruits:
    print("kiwi appeared!")

if fruits:
    print("List has items") # prawda, lista nie jest pusta
else:
    print("List has no items")