"""@package main
Main module for the Python Airport code"""

from PyQt5 import QtWidgets
import airport
import traffic
import simulation
import radarview

## Airport description file name
APT_FILE = "DATA/lfpg_map.txt"
## Flight plans file name
PLN_FILE = "DATA/lfpg_flights.txt"


def main():
    # Load files
    ## Main airport (type airport.Airport)
    apt = airport.from_file(APT_FILE)
    ## Main flights (type traffic.Flight list)
    flights = traffic.from_file(apt, PLN_FILE)

    # create the simulation
    ## Simulation state (type simulation.Simulation)
    sim = simulation.Simulation(apt, flights)

    # Initialize Qt
    ## The main application (type QtWidgets.QApplication)
    app = QtWidgets.QApplication([])

    # create the radar view and the time navigation interface
    ## The main graphical window (type radarview.Radarview)
    main_window = radarview.RadarView(sim)

    print(simulation.SHORTCUTS)

    # enter the main loop
    app.exec_()


if __name__ == "__main__":
    main()
