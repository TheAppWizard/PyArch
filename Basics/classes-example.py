class Calculator:
    def __init__(self, a, b, name):
        self.valueA = a
        self.valueB = b
        self.name = name

        if self.name == "Add":
            self.result = self.add_numbers(self.valueA, self.valueB)

        elif self.name == "Sub":
            self.result = self.subtract_numbers(self.valueA, self.valueB)

        elif self.name == "Mul":
            self.result = self.multiply_numbers(self.valueA, self.valueB)

        elif self.name == "Div":
            self.result = self.divide_numbers(self.valueA, self.valueB)    

    def add_numbers(self, x, y):
        return x + y
    
    def subtract_numbers(self, x, y):
        return x - y
    
    def multiply_numbers(self, x, y):
        return x * y
    
    def divide_numbers(self, x, y):
        return x / y

# Creating an instance of the Calculator class
calculator_result = Calculator(5, 3, "Sub")

print("----------------------------")
print("Py Result:", calculator_result.result) 
print("----------------------------")
