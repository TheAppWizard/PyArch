# Inheritance is like passing on traits from parents to children.
# In our example, Cat and Cow are like children inheriting from the Animal parent.
# The Animal class has a method called speak, but it doesn't have a specific implementation.
# Cat and Cow classes provide their own implementation of speak, which is specific to them.
# So, when a Cat or Cow object speaks, they make their respective sounds.

class Animal:
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print("Meow")

class Cow(Animal):
    def speak(self):
        print("Moo")

# Creating objects of the derived classes
cat = Cat()
cow = Cow()

# Calling the speak method
cat.speak()  # Output: Meow
cow.speak()  # Output: Moo
