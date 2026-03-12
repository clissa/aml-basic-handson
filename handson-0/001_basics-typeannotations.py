# Python Basics: Variables, Data Types, and Control Flow

# Dynamic typing (no need to declare types)
name: str = "Alice"  # String
age: int = "twentyfive"  # Integer
height: float = 1.68   # Float
is_student: bool = True  # Boolean

# List (mutable) and Tuple (immutable)
fruits: list = ["Apple", "Banana", "Cherry"]
coordinates: tuple = (10, 20)

# Dictionary (key-value pairs)
student: dict = {"name": "Alice", "age": 25, "field": "Bioinformatics"}

# Control flow
if age < 30:
    print(f"{name} is young!")

# Looping through a list
for fruit in fruits:
    print(f"I like {fruit}")
