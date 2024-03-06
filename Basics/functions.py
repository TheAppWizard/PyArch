# ---------------------
# Basic Function
# ---------------------

def greet_user():
    print("Hello Python")
greet_user()

# ---------------------
# Passing an argument
# ---------------------

def greet_username(username):
    print("Hello, " + username + "!")
greet_username("Shreyas") # Hello, Shreyas!

# ---------------------
# Default argument
# ---------------------

def make_pizza(topping='bacon'):
    print("Have a " + topping + " pizza!")
make_pizza() #Have a bacon pizza!
make_pizza('pepperoni') #Have a pepperoni pizza!


# ---------------------
# Return
# ---------------------

def add_numbers(x, y):
    return x + y
sum = add_numbers(5, 3)
print(sum) 