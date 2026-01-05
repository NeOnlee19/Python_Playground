# DICTIONARIES

# Empty dictionary
dictionary = {}

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
}

scores = dict(math=95, english=80, science=70)
print(scores) # {'math': 95, 'english': 80, 'science': 70}

# Accessing values
print(person["name"]) # Alice
print(person["age"])  # 30

print(person.get("height")) # None
print(person.get("city", "Unknown")) # Unknown if doesnt exist

# Adding or updating items
person["email"] = "alice@gmail.com"
print(person) # {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': 'alice@gmail.com'}
person["age"] = 20
print(person["age"]) # 20

# Removing items
del person["email"]
age = person.pop("age")
print(person) # {'name': 'Alice', 'city': 'New York'}
person.clear()
print(person) # {}

# Dictionary methods
print(scores.keys()) # dict_keys(['math', 'english', 'science'])
print(scores.values()) # dict_values([95, 80, 70])
print(scores.items()) # dict_items([('math', 95), ('english', 80), ('science', 70)])

if "math" in scores:
    print("math found") # Exist

scores.update({"math": 0, "english": 1}) # Updates multiple values
print(scores) # {'math': 0, 'english': 1, 'science': 70}

# Nested dictionaries
students = {
    "alice": {"age": 20, "grade": 6},
    "bob": {"age": 25, "grade": 2},
    "charlie": {"age": 30, "grade": 3},
}

print(students["alice"]["grade"]) # 6