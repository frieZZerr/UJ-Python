import math

"""Klasa reprezentująca punkty na płaszczyźnie."""
class Point:
	# konstuktor
	def __init__(self, x, y):
		self.x = x
		self.y = y

	# zwraca string "(x, y)"
	def __str__(self):
		result = "({}, {})".format(self.x, self.y)
		return result

	# zwraca string "Point(x, y)"
	def __repr__(self):
		result = "Point({}, {})".format(self.x, self.y)
		return result

	# obsługa point1 == point2
	def __eq__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		return False

	# obsługa point1 != point2
	def __ne__(self, other):
		return not self == other

	# Punkty jako wektory 2D.
	# v1 + v2
	def __add__(self, other):
		result = Point( self.x+other.x, self.y+other.y )
		return result

	# v1 - v2
	def __sub__(self, other):
		result = Point( self.x-other.x, self.y-other.y )
		return result

	# v1 * v2, iloczyn skalarny, zwraca liczbę
	def __mul__(self, other):
		result = self.x*other.x + self.y*other.y
		return result

	# v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
	def cross(self, other):
		return self.x * other.y - self.y * other.x

	# długość wektora
	def length(self):
		result = math.sqrt(self.x**2 + self.y**2)
		return result

	# bazujemy na tuple, immutable points
	def __hash__(self):
		return hash((self.x, self.y))

# Kod testujący moduł.
import unittest

class TestPoint(unittest.TestCase):
	def setUp(self):
		self.zero = Point(0, 0)
		self.point1 = Point(3, 1)
		self.point2 = Point(6, -2)
		self.point3 = Point(-4, -7)
		self.point4 = Point(7, 9)

	def test___str__(self):
		self.assertEqual( self.point1.__str__(), "(3, 1)" )

	def test___repr__(self):
		self.assertEqual( self.point2.__repr__(), "Point(6, -2)" )

	def test___eq__(self):
		self.assertEqual( self.zero.__eq__(self.zero), True )

	def test___ne__(self):
		self.assertEqual( self.zero.__ne__(self.zero), False )

	def test___add__(self):
		self.assertEqual( self.point2.__add__(self.point3), Point(2, -9) )

	def test___sub__(self):
		self.assertEqual( self.point4.__sub__(self.point3), Point(11, 16) )

	def test___mul__(self):
		self.assertEqual( self.point2.__mul__(self.point1), 16 )

	def test_cross(self):
		self.assertEqual( self.point2.cross(self.point1), 12 )

	def test_length(self):
		self.assertEqual( self.point3.length(), math.sqrt(65) )

	def test___hash__(self):
		self.assertEqual( self.point3.__hash__(), hash(self.point3) )

if __name__ == '__main__':
	unittest.main()