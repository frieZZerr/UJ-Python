from points import Point

"""Klasa reprezentująca prostokąt na płaszczyźnie."""
class Rectangle:
	def __init__(self, x1, y1, x2, y2):
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)

	# "[(x1, y1), (x2, y2)]"
	def __str__(self):
		result = "[({}, {}), ({}, {})]".format( self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y )
		return result

	# "Rectangle(x1, y1, x2, y2)"
	def __repr__(self):
		result = "Rectangle({}, {}, {}, {})".format( self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y )
		return result

	# obsługa rect1 == rect2
	def __eq__(self, other):
		if self.pt1 == other.pt1 and self.pt2 == other.pt2:
			return True
		return False

	# obsługa rect1 != rect2
	def __ne__(self, other):
		return not self == other

	# zwraca środek prostokąta
	def center(self):
		x = (self.pt1.x+self.pt2.x) / 2
		y = (self.pt1.y+self.pt2.y) / 2
		result = Point( x, y )
		return result

	# pole powierzchni
	def area(self):
		x = self.pt1.x-self.pt2.x
		y = self.pt1.y-self.pt2.y
		result = abs(x*y)
		return result

	# przesunięcie o (x, y)
	def move(self, x, y):
		result = Rectangle( self.pt1.x+x, self.pt1.y+y, self.pt2.x+x, self.pt2.y+y )
		return result

# Kod testujący moduł.
import unittest

class TestRectangle(unittest.TestCase):
	def setUp(self):
		self.zero = Rectangle( 0, 0, 0, 0 )
		self.rec1 = Rectangle( 2, 1, 4, 2 )
		self.rec2 = Rectangle( -3, 4, -1, -2 )
		self.rec3 = Rectangle( 1, -1, 3, -3 )

	def test___str__(self):
		self.assertEqual( self.zero.__str__(), "[(0, 0), (0, 0)]" )

	def test___repr__(self):
		self.assertEqual( self.rec1.__repr__(), "Rectangle(2, 1, 4, 2)" )

	def test___eq__(self):
		self.assertEqual( self.rec2.__eq__(self.rec2), True )

	def test___ne__(self):
		self.assertEqual( self.rec2.__ne__(self.rec2), False )

	def test_center(self):
		self.assertEqual( self.rec2.center(), Point(-2, 1) )

	def test_area(self):
		self.assertEqual( self.rec3.area(), 4 )

	def test_move(self):
		self.assertEqual( self.rec3.move( 2, 2 ), Rectangle( 3, 1, 5, -1 ) )

if __name__ == '__main__':
	unittest.main()