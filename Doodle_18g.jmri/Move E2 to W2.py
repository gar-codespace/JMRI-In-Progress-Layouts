# Author: Daniel Boudreau, copyright 2011
#
# Modified by Greg Ritacco November 2015
# Modified by Greg Ritacco July 2021
# Modified by Greg Ritacco July 2023

"""
Special script for Doodle 18 moves RS:
from Staging E2 to Staging W2.
"""
import jmri

class setCars(jmri.jmrit.automat.AbstractAutomaton):
    def init(self):
    # Boilerplate
        self.LM = jmri.InstanceManager.getDefault(jmri.jmrit.operations.locations.LocationManager)
        self.CM = jmri.InstanceManager.getDefault(jmri.jmrit.operations.rollingstock.cars.CarManager)
        self.EM = jmri.InstanceManager.getDefault(jmri.jmrit.operations.rollingstock.engines.EngineManager)
    # Edit these for your layout
        self.startPointLocation = "Easton" # To Location
        self.startPointTrack = "E2"
        self.startPointTrackType = 'Staging'

        self.endpointLocation = "Weston" # From location
        self.endpointTrack = "W2"
        self.endpointTrackType = 'Staging'

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
            endpointLocation = self.LM.getLocationByName(self.endpointLocation)
        except:
            print('Not a valid location: ' + self.endpointLocation)
            return False
        try:
            endpointTrack = endpointLocation.getTrackByName(self.endpointTrack, self.endpointTrackType)
        except:
            print('Not a valid track/type: ' + self.endpointTrack + self.endpointTrackType)
            return False

    # If the location and track are OK, move the cars and engines from staging to the interchange
        carList = self.CM.getByIdList()
        engineList = self.EM.getByIdList()
        i = 0

        for car in carList:
            if (car.getLocationName() == self.startPointLocation and car.getTrackName() == self.startPointTrack):
                car.setLocation(endpointLocation, endpointTrack)
                print("Car ", car.getRoadName() + car.getNumber(), " set to Location: ", endpointLocation.toString(), ", Track: ", endpointTrack.toString())
                i += 1

        j = 0
        for engine in engineList:
            if (engine.getLocationName() == self.startPointLocation and engine.getTrackName() == self.startPointTrack):
                engine.setLocation(endpointLocation, endpointTrack)
                print("Engine ", engine.getRoadName() + engine.getNumber(), " set to Location: ", endpointLocation.toString(), ", Track: ", endpointTrack.toString())
                j += 1

        print('Cars moved: ', i, ' Engines moved: ', j)

        return False              #False means run this only once

setCars().start()
print('Done')
