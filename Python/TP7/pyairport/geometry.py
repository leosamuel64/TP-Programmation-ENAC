"""@package geometry
Geometry classes and utilities."""


class Point:
    """A point described by its coordinates in meter"""

    def __init__(self, x, y):
        """The constructor
        @param x,y @e int: Coordinates of the point"""
        ## x-coordinate (meter)
        self.x = x
        ## y-coordinate (meter)
        self.y = y

    def __repr__(self):
        return "({0.x}, {0.y})".format(self)

    def __sub__(self, other):
        """Vector subtraction"""
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        """Vector addition"""
        return Point(self.x + other.x, self.y + other.y)

    def __rmul__(self, k):
        """Vector multiplication by a scalar"""
        return Point(k * self.x, k * self.y)

    def __abs__(self):
        """Vector norm"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def sca(self, other):
        """Scalar product of two vectors"""
        return self.x * other.x + self.y * other.y

    def det(self, other):
        """Determinant of two vectors"""
        return self.x * other.y - self.y * other.x

    def distance(self, other):
        """Distance between two points"""
        return abs(self - other)

    def seg_dist(self, a, b):
        """Distance from point to segment
        @param a,b @e Point: Description of segment
        @return Distance from Point self to segment [a, b]"""
        ab, ap, bp = b - a, self - a, self - b
        if ab.sca(ap) <= 0:
            return abs(ap)
        elif ab.sca(bp) >= 0:
            return abs(bp)
        else:
            return abs(ab.det(ap)) / abs(ap)


class PolyLine:
    """A poly-line described by a series of points"""

    def __init__(self, coords):
        """The constructor
        @param coords @e Point list: the points describing the poly-line"""
        ## Length of the poly-line (meter)
        self.length = sum(pi.distance(coords[i - 1])
                          for i, pi in enumerate(coords[1:]))
        ## Points in the poly-line
        self.coords = coords

    def __repr__(self):
        return "<geometry.Line {}>".format(len(self))

    def __str__(self):
        points = ', '.join(str(p) for p in self.coords)
        return 'PolyLine {}m: ({})'.format(self.length, points)

    def __len__(self):
        return len(self.coords)
