# Author: Daniel Boudreau, copyright 2011
#
# Modified by Greg Ritacco November 2015
# Modified by Greg Ritacco July 2021

import jmri

class setCars(jmri.jmrit.automat.AbstractAutomaton):
    def init(self):
    # Boilerplate
        self.lm = jmri.InstanceManager.getDefault(jmri.jmrit.operations.locations.LocationManager)
        self.cm = jmri.InstanceManager.getDefault(jmri.jmrit.operations.rollingstock.cars.CarManager)
        self.em = jmri.InstanceManager.getDefault(jmri.jmrit.operations.rollingstock.engines.EngineManager)
    # Edit these for your layout
        self.fromLocation = "Easton" # From location
        self.fromTrack = "E2"
        self.fromTrackType = 'Staging'

        self.toLocation = "Weston" # To Location
        self.toTrack = "W2"
        self.toTrackType = 'Staging'

        return

    def handle(self):
    # check the location and track
        if (self.lm.getLocationByName(self.toLocation) and self.lm.getLocationByName(self.toLocation).getTrackByName(self.toTrack, self.fromTrackType)):
            print('To location (' + self.toLocation + ') and Track (' + self.toTrack + ') is valid')
        else:
            print('To location (' + self.toLocation + ') and Track (' + self.toTrack + ') is not valid')
            return False
        if (self.lm.getLocationByName(self.fromLocation) and self.lm.getLocationByName(self.fromLocation).getTrackByName(self.fromTrack, self.toTrackType)):
            print('To location (' + self.fromLocation + ') and Track (' + self.fromTrack + ') is valid')
        else:
            print('To location (' + self.fromLocation + ') and Track (' + self.fromTrack + ') is not valid')
            return False

    # If the location and track are OK, move the cars and engines
        carList = self.cm.getByIdList()
        engineList = self.em.getByIdList()
        i = 0
        for car in carList:
            if (car.getLocationName() == self.fromLocation and car.getTrackName() == self.fromTrack):
                setLocation = self.lm.getLocationByName(self.toLocation)
                setTrack = setLocation.getTrackByName(self.toTrack, self.toTrackType)
                car.setLocation(setLocation, setTrack)
                print("Car", car.getRoadName() + car.getNumber(), "set to Location:", car.getLocationName(),", Track:", car.getTrackName())
                i += 1

        j = 0
        for engine in engineList:
            if (engine.getLocationName() == self.fromLocation and engine.getTrackName() == self.fromTrack):
                setLocation = self.lm.getLocationByName(self.toLocation)
                setTrack = setLocation.getTrackByName(self.toTrack, self.toTrackType)
                engine.setLocation(setLocation, setTrack)
                print("Engine", engine.getRoadName() + engine.getNumber(), "set to Location:", engine.getLocationName(),", Track:", engine.getTrackName())
                j += 1

        print('Cars moved:',i, 'Engines moved:',j)
        return False              #False means run this only once

setCars().start()
print('Done')
