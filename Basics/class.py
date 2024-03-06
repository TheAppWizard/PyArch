class Calculator:
    def __init__(self, a, b):
        self.valueA = a
        self.valueB = b

    def add(self):
        print(f"Added = {self.valueA + self.valueB}")

    def subtract(self):
        print(f"Subtracted = {self.valueA - self.valueB}")

    def multiply(self):
        print(f"Multiplied = {self.valueA * self.valueB}")

    def divide(self):
        if self.valueB == 0:
            print("Cannot divide by zero")
        else:
            print(f"Divided = {self.valueA / self.valueB}")

# Creating an instance of the Calculator class
calculate = Calculator(10, 2)

# Calling the various methods
calculate.add()       # Output: Added = 12
calculate.subtract()  # Output: Subtracted = 8
calculate.multiply()  # Output: Multiplied = 20
calculate.divide()    # Output: Divided = 5.0
