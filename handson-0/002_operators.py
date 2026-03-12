# Arithmetic and Comparison
a = 10
b = 3
print(a + b)  # 13
print(a / b)  # 3.333
print(a // b) # 3 (floor division)
print(a > b)  # True

# Logical and Membership
x = [1, 2, 3]
print(2 in x)     # True
print(4 not in x) # True

# Identity Operators
y = x
print(x is y)  # True (same object reference)
z = [1, 2, 3]
z = x.copy()
print(x == z)  # True (same values)
print(x is z)  # False (different object reference)

y.append(4)
print(x)

z = [1, 2, 3]
if x is z:
    print(f"x is z gives {x is z}: same object reference")
elif x == z:
    print(f"x is z gives {x is z}, but x==z is {x==z}:\nsame values but different object reference")
else:
    print("x and z are totally different")  