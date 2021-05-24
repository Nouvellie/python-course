import math


class Circle(object):
    "An advanced circle analytic toolkit"

    __slots__ = ['diameter']
    VERSION = '0.1'

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        "Perform quadrature on a shape of uniform radius"
        # return math.pi * self.radius ** 2.0
        p = self.perimeter()
        r = p / math.pi / 2.0
        return math.pi * r ** 2.00

    def perimeter(self):
        return 2.0 * math.pi * self.radius
    
    # _perimeter = perimeter

    @property
    def radius(self):
        "Radius of a circle"
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    @classmethod
    def from_bbd(cls, bbd):
        "Construct a circle from a bounding box diagonal"
        radius = bbd / 2.0 / math.sqrt(2.0)
        # return Circle(radius)
        return cls(radius)

    @staticmethod
    def angle_to_grade(angle):
        "Convert angle in degree to a percentage grade"
        return math.tan(math.radians(angle)) * 100.0


# Instance Tire again to get angle_to_grade staticmethod
class Tire(Circle):
    "Tires are circles with a corrected perimeter"

    def perimeter(self):
        "Circumference corrected for the rubber"
        return Circle.perimeter(self) * 1.25
    
    # _perimeter = perimeter