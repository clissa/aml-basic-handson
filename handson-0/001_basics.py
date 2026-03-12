# Python Basics: Variables, Data Types, and Control Flow

# Dynamic typing (no need to declare types)
name = "Alice"  # String
second_name = 'Bob'
age = 25        # Integer
height = 1.68   # Float
is_student = True  # Boolean

# List (mutable) and Tuple (immutable)
fruits = ["Apple", "Banana", "Cherry"]
coordinates = (10, 20)


# Dictionary (key-value pairs)
student = {"name": "Alice", "age": 25, "field": "Bioinformatics"}

# Control flow
if age > 30:
    print(f"{name} is young!")
else:
    print("not true...")

# Looping through a list
for fruit in fruits:
    print(f"I like {fruit}")