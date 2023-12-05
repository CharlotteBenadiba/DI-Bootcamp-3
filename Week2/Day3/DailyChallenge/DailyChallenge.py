# Daily Challenge - Circle
# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

# from math import pi

#class Circle:
#    def __init__(self, radius=None, diameter=None):
#        if radius is not None and diameter is not None:
#            raise ValueError("Both radius and diameter cannot be specified.")
#        if radius is None and diameter is None:
#            raise ValueError("Either radius or diameter must be specified.")
        
#        if radius is not None:
#            self.radius = radius
#        else:
#            self.radius = diameter / 2.0

#    @property
#    def diameter(self):
#        return self.radius * 2

#    @property
#    def area(self):
#        return pi * self.radius ** 2

#    def __str__(self):
#        return f"Circle: Radius = {self.radius}, Diameter = {self.diameter}, Area = {self.area}"

#    def __add__(self, other):
#        return Circle(radius=self.radius + other.radius)

#    def __lt__(self, other):
#        return self.radius < other.radius

#    def __eq__(self, other):
#        return self.radius == other.radius

# circle1 = Circle(radius=5)
# circle2 = Circle(diameter=10)
# print(circle1)
# print(circle2)
# print(f"Circle 1 + Circle 2: {circle1 + circle2}")

# circles = [Circle(radius=3), Circle(radius=1), Circle(radius=2)]
# sorted_circles = sorted(circles)
# print("Sorted Circles:")
#for circle in sorted_circles:
#    print(circle)
