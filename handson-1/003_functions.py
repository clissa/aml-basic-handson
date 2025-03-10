addends: list = [0, 1, 2, 3, 4, 5]
course_title: str = "Welcome to AML! Hope you enjoy :)"

### Standard functions
sum(addends)
print(course_title)
print(course_title.upper())


### User defined functions


# Function without parameters
def greet():
    print("Hello, welcome to AML course!\nDo you have any question?")


greet()  # Calling the function


# Function with parameters and return value
def subtract_numbers(a, b):
    return a - b

result = subtract_numbers(5, 7)
print(result)  # -2

# Function with parameters and return value
def type_annotated_subtract_numbers(a: int, b: int) -> int:
    res = a-b
    print(f"{res=}\t{type(res)=}")
    return res

typed_result = type_annotated_subtract_numbers(8, 3)

# but it works even if we mess up
typed_result = type_annotated_subtract_numbers(1_000_000, 987_654_321.12)


# Function with default parameter
def greet_user(name="Guest"):
    print(f"Hello, {name.title()}!\nHow can I help you?")


greet_user()  # default
greet_user("Alice")  # customized
greet_user("alice IN w0ND3rl4nd")  # customized