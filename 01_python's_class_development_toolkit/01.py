import math


class Circle(object):
	"An advanced circle analytic toolkit"

	__slots__ = ['diameter']
	version = "0.1.0"


	def __init__(self, radius):
		self.radius = radius


	def area(self):
		"Perform quadrature on a shape of uniform radius"
		# return math.pi * self.radius ** 2.0
		p = self.perimeter()
		r = p / math.pi / 2.0
		return math.pi  * r ** 2.0


	def perimeter(self):
		return 2.0 * math.pi * self.radius


	@property
	def radius(self):
		"Radius of a circle"
		return self.diameter / 2.0

	@radius.setter
	def radius(self, radius):
		self.diameter = radius * 2.0


	@staticmethod
	def angle_to_grade(angle):
		"Convert angle in degree to a percentage grade"
		return math.tan(math.radians(angle)) * 100.0


	@classmethod
	def from_bdd(cls, bdd):
		"Construct a circle from a bounding box diagonal"
		radius = bdd / 2.0 / math.sqrt(2.0)
		return Circle(radius)


class Tire(Circle):
	"Tires are circle with a corrected perimeter"


	def perimeter(self):
		"Circumference corrected for the rubber"
		return Circle.perimeter(self) * 1.25