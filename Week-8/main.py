from points import Point
from circles import Circle

def test_from_points():
    circle = Circle.from_points([Point(-6, 3), Point(-3, 2), Point(0, 3)])
    assert str(circle) == 'Circle( -3.0, 7.0, 5.0 )'

def test_properties():
    circle = Circle( 0, 0, 2 )

    assert circle.top    == 2
    assert circle.bottom == -2

    assert circle.left  == -2
    assert circle.right == 2

    assert circle.width  == 4
    assert circle.height == 4

    assert circle.topleft    == Point( -2, 2  )
    assert circle.bottomleft == Point( -2, -2 )

    assert circle.topright    == Point( 2, 2  )
    assert circle.bottomright == Point( 2, -2 )

if __name__ == '__main__':
    test_properties()
    test_from_points()