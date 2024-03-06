# Encapsulation is like putting things in a box and allowing access only through specific means.
# In our example, Person has attributes like name and age.
# We use methods like get_name and set_age to access and modify these attributes, respectively.
# The attributes are marked as _name and _age, indicating they're meant to be accessed or modified using these methods.
# This helps in controlling how data is accessed and modified, ensuring data integrity and security.

class Person:
    def __init__(self, name, age):
        self._name = name  # Private attribute
        self._age = age

    def get_name(self):  # Getter method
        return self._name

    def set_age(self, age):  # Setter method
        if age > 0:
            self._age = age

# Creating an object of the Person class
person = Person("Shreyas", 30)

# Accessing attributes using getter and setter methods
print(person.get_name())  # Output: Alice
person.set_age(25)
print(person._age)        # Output: 25 (not recommended, should use getter)
