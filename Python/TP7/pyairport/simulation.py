"""@package simulation
Interactive airport simulation.

This module defines the interactions with the simulation"""

import traffic

## Keyboard shortcuts
SHORTCUTS = """Shortcuts:
f: go forward
b: go backward
space: play/pause
q: quit"""


class Simulation:
    """The simulation state """

    def __init__(self, apt, flights, init_time = traffic.DAY // 2):
        """The constructor """
        ## The airport (type airport.Airport)
        self.airport = apt
        ## The flights (type traffic.Flight list)
        self.all_flights = flights
        ## Conflicts at current time (dict)
        self.conflicts = {}
        ## Current time step (type int)
        self.t = init_time
        ## The flights at current time (type traffic.Flight list)
        self.current_flights = traffic.select(self.all_flights, self.t)

    def set_time(self, t):
        """Sets the current time of the simulation
        @param t @e int: a time step """
        self.t = t
        self.current_flights = traffic.select(self.all_flights, self.t)

    def increment_time(self, dt):
        """Advance time by a given amount
        @param dt @e int: number of time steps (might be < 0) """
        self.set_time(self.t + dt)
