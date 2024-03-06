# Polymorphism means different shapes or forms.
# In our example, Circle and Square are shapes that inherit from the Shape parent.
# Each shape has its own way of being drawn, defined by the draw method.
# When we call draw_shape, it accepts any shape as an argument.
# Despite having different implementations of draw,
#  we can treat both Circle and Square objects similarly and draw them without knowing their specific type.

class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Square(Shape):
    def draw(self):
        print("Drawing Square")

def draw_shape(shape):
    shape.draw()

# Using draw_shape function with different types of shapes
circle = Circle()
square = Square()

draw_shape(circle)  # Output: Drawing Circle
draw_shape(square)  # Output: Drawing Square
