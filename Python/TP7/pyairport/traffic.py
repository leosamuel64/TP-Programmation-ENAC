"""@package traffic
Traffic sample description.

This module allows to load a traffic file
and to access all its flights information.
"""


import enum
import airport

## Time step (seconds)
STEP = 5
## Day duration in time steps
DAY = 24 * 3600 // STEP
## Minimal separation (meters)
SEP = 70
## Runway area width (meters)
RWY_SEP = 90


class Movement(enum.Enum):
    """Type of movements on the airport"""
    ## Departure
    DEP = 1
    ## Arrival
    ARR = 2


def movement_from_string(s):
    if s == 'DEP':
        return Movement.DEP
    elif s == 'ARR':
        return Movement.ARR


class Flight:
    """Flight information"""

    def __init__(self, call_sign, flight_type, cat):
        """The constructor """
        ## Commercial call sign (type: str)
        self.call_sign = call_sign
        ## Departure or arrival (type: Movement)
        self.type = flight_type
        ## Wake vortex category (type: airport.WakeVortexCategory)
        self.cat = cat
        ## Parking stand at departure or on arrival (type: airport.NamedPoint)
        self.stand = None
        ## Take-off or landing runway (type: airport.Runway)
        self.runway = None
        ## Runway direction (type: int = 0 or 1)
        self.qfu = 0
        ## Time of first trajectory point in the simulation (type: int)
        self.start_t = None
        ## Runway occupation time (type: int)
        self.rwy_t = None
        ## Take-off slot (NMOC) time, if any (type: None or int)
        self.slot = None
        ## Route as a sequence of points (type: geometry.Point tuple)
        self.route = None

    def __repr__(self):
        return "<traffic.Flight {0}>".format(self.call_sign)

    def get_position(self, t):
        """Access the aircraft position at a given time
        @param t @e int: a time stamp
        @return the position of the aircraft at time t"""
        return self.route[t - self.start_t]


# Time string conversions

def hms(t):
    """Get the time of day corresponding to a time step in the simulation
    @param t @e int: a time step
    @return a time as a string of the form HH:MM:SS"""
    s = t * STEP
    return "{:02d}:{:02d}:{:02d}".format(s // 3600, s // 60 % 60, s % 60)


def time_step(hms):
    """Get a time step in the simulation from a given time in the day
    @param hms @e str: a time in the day, of the form HH:MM:SS
    @return a time step (int)"""
    l = hms.replace(':', ' ').split() + [0, 0, 0]
    return (int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])) // STEP


# Load a traffic file

def from_file(apt, filename):
    """Parse a traffic file to extract flight plan informations
    @param apt @e airport.Airport: the airport
    @param filename @e str: the name of the file containing the flight plans
    @return a Flight list"""
    categories = {'L': airport.WakeVortexCategory.LIGHT,
                  'M': airport.WakeVortexCategory.MEDIUM,
                  'H': airport.WakeVortexCategory.HEAVY}
    print("Loading traffic:", filename + '...')
    file = open(filename)
    flights = []
    for line in file:
        words = line.strip().split()
        movement_type = movement_from_string(words[0])
        flight = Flight(words[1], movement_type, categories[words[2]])
        flight.stand = airport.get_point(apt, words[3])
        flight.qfu = airport.get_qfu(apt, words[4])
        flight.runway = airport.get_runway(apt, flight.qfu)
        flight.rwy_t = int(words[6]) // STEP
        flight.slot = None if words[7] == '_' else int(words[7]) // STEP
        flight.route = airport.xys_to_points(words[8:])
        flight.start_t = int(words[5]) // STEP
        flights.append(flight)
    file.close()
    return flights


def select(flights, t):
    """Selects the flights that are moving at a given time step
    @param flights @e Flight list: a list of flights to select from
    @param t @e int: a time step
    @return a Flight list"""
    selection = []
    for f in flights:
        if f.start_t <= t < f.start_t + len(f.route):
            selection.append(f)
    return selection
