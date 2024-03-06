# ---------------------
# Basic if statement
# ---------------------

x = 10
if x > 5:
    print("x is greater than 5")



# ---------------------
# if else statement
# ---------------------

x = 3
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")


# ---------------------
# if else if else statement
# ---------------------

score = 69
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# ---------------------
# Nested statement
# ---------------------

x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
    else:
        print("x is greater than or equal to 15")
else:
    print("x is less than or equal to 5")


# ---------------------
# Using logical operators
# ---------------------

x = 10
y = 60
if x > 5 and y < 30:
    print("Both conditions are true")
elif x > 5 or y > 30:
    print("At least one condition is true")
else:
    print("No condition is true")

# ---------------------
# Ternary operator
# ---------------------

x = 10
result = "even" if x % 2 == 0 else "odd"
print(f"x is {result}")



