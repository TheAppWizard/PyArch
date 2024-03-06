# Think of a class as a blueprint or a template for creating objects.
# In the example of the Dog class, imagine it as a blueprint for creating different types of dogs.
# Each dog created from this blueprint has a name and can bark.
# dog1 and dog2 are two different dogs created from the Dog blueprint.

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects of the Dog class
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# Accessing attributes and calling methods
print(dog2.name)  # Output: Buddy
dog2.bark()       # Output: Max says Woof!
