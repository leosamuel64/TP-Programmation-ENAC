"""@package airport
Airport elements description.

This module allows to read an airport description file
and access all its elements information."""

import enum
import geometry


class PointType(enum.Enum):
    """The type of points found on an airport"""
    ## Parking stand
    STAND = 1
    ## Winter is coming
    DEICING = 2
    ## Access point to a runway
    RUNWAY_POINT = 3


class WakeVortexCategory(enum.Enum):
    """Wake vortex categories"""
    ## Light <= 7000 kg
    LIGHT = 1
    ## 7000 kg < Medium < 136000 kg
    MEDIUM = 2
    ## 136000 kg <= Heavy
    HEAVY = 3


## Runways area
RUNWAY_WIDTH = 90
## Taxiways area
TAXIWAY_WIDTH = 15


class NamedPoint(geometry.Point):
    """Named point of the airport"""

    def __init__(self, name, pt_type, point):
        """The constructor """
        x, y = map(int, point.split(','))
        super().__init__(x, y)
        ## Name of the point (@e str)
        self.name = name
        ## Type of point (@e PointType)
        self.type = pt_type

    def __repr__(self):
        return "<airport.NamedPoint {0}>".format(self.name)


class Taxiway(geometry.PolyLine):
    """Taxiway portion of the airport """

    def __init__(self, taxi_name, speed, cat, one_way, coords):
        """The constructor """
        super().__init__(coords)
        ## Name of the taxiway that it belongs to (type str)
        self.taxi_name = taxi_name
        ## Maximum speed on the portion in m/s (type int)
        self.speed = speed
        ## Maximum allowed wake vortex category (type WakeVortexCategory)
        self.cat = cat
        ## Is it a one-way portion? (type boolean)
        self.one_way = one_way

    def __repr__(self):
        return "<airport.Taxiway {0}>".format(self.taxi_name)


class Runway(geometry.PolyLine):
    """Runway of the airport """

    def __init__(self, name, qfu1, qfu2, ends, named_points):
        """The constructor """
        super().__init__(ends)
        ## Name of the runway (type str)
        self.name = name
        ## Runway directions (type str tuple)
        self.qfus = (qfu1, qfu2)
        ## The points on the runway (type NamedPoint tuple)
        self.named_points = named_points

    def __repr__(self):
        return "<airport.Runway {0}>".format(self.name)


class Airport:
    """Whole airport description """

    def __init__(self, name, points, taxiways, runways):
        """The constructor """
        ## Airport name (type str)
        self.name = name
        ## Points on the airport (type NamedPoint tuple)
        self.points = points
        ## Taxi-way portions (type Taxiways tuple)
        self.taxiways = taxiways
        ## Runways (type Runway tuple)
        self.runways = runways

    def __repr__(self):
        return "<airport.Airport {0}>".format(self.name)


# Reading an airport file

def xys_to_points(xy_list):
    """Converts a list of strings to proper points
    @param xy_list @e str @e list: list of points as 'x,y'
    @return a Point tuple """

    def xy_to_point(xy):
        x, y = map(int, xy.split(','))
        return geometry.Point(x, y)

    points = []
    for xy in xy_list:
        points.append(xy_to_point(xy))
    return tuple(points)


def from_file(filename):
    """Parse an airport file to extract information
    @param filename @e str: the file containing the airport description
    @return an Airport """
    print("Loading airport", filename + '...')
    file = open(filename)
    categories = {'L': WakeVortexCategory.LIGHT,
                  'M': WakeVortexCategory.MEDIUM,
                  'H': WakeVortexCategory.HEAVY}
    point_types = [PointType.STAND, PointType.DEICING, PointType.RUNWAY_POINT]
    name = file.readline().strip()
    points, taxiways, runways = [], [], []
    for line in file:
        words = line.strip().split()
        if words[0] == 'P':  # Point description
            pt_type = point_types[int(words[2])]
            points.append(NamedPoint(words[1], pt_type, words[3]))
        elif words[0] == 'L':  # Taxiway description
            speed = int(words[2])
            cat = categories[words[3]]
            one_way = words[4] == 'S'
            xys = xys_to_points(words[5:])
            taxiways.append(Taxiway(words[1], speed, cat, one_way, xys))
        elif words[0] == 'R':  # Runway description
            pts = tuple(words[4].split(','))
            xys = xys_to_points(words[5:])
            runways.append(Runway(words[1], words[2], words[3], xys, pts))
    file.close()
    return Airport(name, tuple(points), tuple(taxiways), tuple(runways))


def get_point(apt, name):
    """Search an airport for a point with a given name
    @param apt @e Airport: the airport to search
    @param name @e str: the name of the searched point
    @return a NamedPoint or None if the name was not found """
    for point in apt.points:
        if point.name == name:
            return point


def get_runway(apt, name):
    """Search an airport for a runway with a given name
    @param apt @e Airport: the airport to search
    @param name @e str: the name of the searched runway
    @return a Runway or None if the name was not found """
    for rwy in apt.runways:
        if name == rwy.qfus[0] or name == rwy.qfus[1]:
            return rwy


def get_qfu(apt, name):
    """Search an airport for a runway direction with a given name
    @param apt @e Airport: the airport to search
    @param name @e str: the name of the searched runway direction
    @return a QFU (@e str) or None if the name was not found """
    for rwy in apt.runways:
        if name == rwy.qfus[0] or name == rwy.qfus[1]:
            return name
