# Author: Daniel Boudreau, copyright 2011
#
# Modified by Greg Ritacco November 2015
# Modified by Greg Ritacco July 2021
# Modified by Greg Ritacco July 2023

"""
Special script for Doodle 18 moves RS:
from Summit interchange to Overton staging,
from Overton staging then back to Summit interchange.
"""
import jmri

class setCars(jmri.jmrit.automat.AbstractAutomaton):
    def init(self):
    # Boilerplate
        self.LM = jmri.InstanceManager.getDefault(jmri.jmrit.operations.locations.LocationManager)
        self.CM = jmri.InstanceManager.getDefault(jmri.jmrit.operations.rollingstock.cars.CarManager)
        self.EM = jmri.InstanceManager.getDefault(jmri.jmrit.operations.rollingstock.engines.EngineManager)
    # Edit these for your layout
        self.startPointLocation = "Overton" # From location
        self.startPointTrack = "O1"
        self.startPointTrackType = 'Staging'

        self.endPointLocation = "Summit" # To Location
        self.endPointTrack = "S1"
        self.endPointTrackType = 'Interchange'

        return

    def handle(self):
    # check the location and track
        try:
            startPointLocation = self.LM.getLocationByName(self.startPointLocation)
        except:
            print('Not a valid location: ' + self.startPointLocation)
            return False
        try:
            startPointTrack = startPointLocation.getTrackByName(self.startPointTrack, self.startPointTrackType)
        except:
            print('Not a valid track/type: ' + self.startPointTrack + self.startPointTrackType)
            return False

        try:
            endPointLocation = self.LM.getLocationByName(self.endPointLocation)
        except:
            print('Not a valid location: ' + self.endPointLocation)
            return False
        try:
            endPointTrack = endPointLocation.getTrackByName(self.endPointTrack, self.endPointTrackType)
        except:
            print('Not a valid track/type: ' + self.endPointTrack + self.endPointTrackType)
            return False


    # If the location and track are OK, move the cars and engines from staging to the interchange
        carList = self.CM.getByIdList()
        engineList = self.EM.getByIdList()
        i = 0

        for car in carList:
            if (car.getLocationName() == self.startPointLocation and car.getTrackName() == self.startPointTrack):
                car.setLocation(endPointLocation, endPointTrack)
                # print("Car ", car.getRoadName() + car.getNumber(), " set to Location: " , endPointLocation.toString(), ", Track: ", endPointTrack.toString())
                i += 1

        j = 0
        for engine in engineList:
            if (engine.getLocationName() == self.startPointLocation and engine.getTrackName() == self.startPointTrack):
                engine.setLocation(endPointLocation, endPointTrack)
                # print("Engine ", engine.getRoadName() + engine.getNumber(), " set to Location: ", endPointLocation.toString(), ", Track: ", endPointTrack.toString())
                j += 1

        print('Cars moved:', i, 'Engines moved:', j)

        return False              #False means run this only once

setCars().start()
print('Done')
