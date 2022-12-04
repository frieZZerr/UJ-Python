import math
from cmath import pi
from points import Point

"""Klasa reprezentująca okręgi na płaszczyźnie."""
class Circle:
    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Nie udalo sie utworzyc okregu z ujemnym promieniem")

        self.pt     = Point( x, y )
        self.radius = radius

    # "Circle(x, y, radius)"
    def __repr__(self):
        return "Circle( %s, %s, %s )" % ( self.pt.x, self.pt.y, self.radius )

    def __eq__(self, other):
        return isinstance( other, Circle ) and self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    # pole powierzchni
    def area(self):
        return pi*self.radius**2

    # przesuniecie o (x, y)
    def move(self, x, y):
        return Circle( self.pt.x+x, self.pt.y+y, self.radius )

    # najmniejszy okrąg pokrywający oba
    def cover(self, other):
        if not isinstance( other, Circle ):
            raise TypeError("Nie udalo sie utworzyc okregu poniewaz jeden z nich nie jest okregiem")

        dx = other.pt.x - self.pt.x
        dy = other.pt.y - self.pt.y
        dc = math.sqrt( dx**2 + dy**2 )

        rmin = min( self.radius, other.radius )
        rmax = max( self.radius, other.radius )

        if rmax > rmin+dc:
            if self.radius > other.radius:
                x = self.pt.x
                y = self.pt.y
            else:
                x = other.pt.x
                y = other.pt.y

            R = rmax
        else:
            R = (self.radius+other.radius+dc)  / 2
            x = self.pt.x + (R-self.radius)*dx / dc
            y = self.pt.y + (R-self.radius)*dy / dc

        return Circle( x, y, R )
    
    @classmethod
    def from_points( cls, points ):
        if not isinstance( points, (list, tuple) ):
            raise TypeError("Punkty zostaly podane w zlym formacie")

        a = points[0].x*(points[1].y-points[2].y) - points[0].y*(points[1].x-points[2].x) + points[1].x*points[2].y - points[2].x*points[1].y
        b = ( points[0].x**2 + points[0].y**2 )*( points[2].y-points[1].y ) + ( points[1].x**2 + points[1].y**2 )*( points[0].y-points[2].y ) + ( points[2].x**2 + points[2].y**2 )*( points[1].y-points[0].y )
        c = ( points[0].x**2 + points[0].y**2 )*( points[1].x-points[2].x ) + ( points[1].x**2 + points[1].y**2 )*( points[2].x-points[0].x ) + ( points[2].x**2 + points[2].y**2 )*( points[0].x-points[1].x )
        d = ( points[0].x**2 + points[0].y**2 )*( points[2].x*points[1].y - points[1].x*points[2].y ) + ( points[1].x**2 + points[1].y**2 )*( points[0].x*points[2].y - points[2].x*points[0].y ) + ( points[2].x**2 + points[2].y**2 )*( points[1].x*points[0].y - points[0].x*points[1].y )
       
        x = -b / (2*a)
        y = -c / (2*a)
        R = math.sqrt( (b**2 + c**2 - 4*a*d) / (4 * a**2) )
        
        return cls( x, y, R )

    @property
    def top(self):
        return self.pt.y+self.radius

    @property
    def bottom(self):
        return self.pt.y-self.radius

    @property
    def left(self):
        return self.pt.x-self.radius

    @property
    def right(self):
        return self.pt.x+self.radius

    @property
    def width(self):
        return 2*self.radius

    @property
    def height(self):
        return 2*self.radius

    @property
    def topleft(self):
        return Point( self.pt.x-self.radius, self.pt.y+self.radius )

    @property
    def bottomleft(self):
        return Point( self.pt.x-self.radius, self.pt.y-self.radius )

    @property
    def topright(self):
        return Point( self.pt.x+self.radius, self.pt.y+self.radius )

    @property
    def bottomright(self):
        return Point( self.pt.x+self.radius, self.pt.y-self.radius )