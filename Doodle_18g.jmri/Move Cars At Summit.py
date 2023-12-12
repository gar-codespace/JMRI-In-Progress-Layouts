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
        self.endpointLocation = "Summit" # From location
        self.endpointTrack = "S2"
        self.endpointTrackType = 'Interchange'

        self.midpointLocation = "Overton" # To Location
        self.midpointTrack = "S1"
        self.midpointTrackType = 'Staging'

        return

    def handle(self):
    # check the location and track
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

        try:
            midpointLocation = self.LM.getLocationByName(self.midpointLocation)
        except:
            print('Not a valid location: ' + self.midpointLocation)
            return False
        try:
            midpointTrack = midpointLocation.getTrackByName(self.midpointTrack, self.midpointTrackType)
        except:
            print('Not a valid track/type: ' + self.midpointTrack + self.midpointTrackType)
            return False


    # If the location and track are OK, move the cars and engines from the interchange to staging
        carList = self.CM.getByIdList()
        engineList = self.EM.getByIdList()
        i = 0

        for car in carList:
            if (car.getLocationName() == self.endpointLocation and car.getTrackName() == self.endpointTrack):
                car.setLocation(midpointLocation, midpointTrack)
                print("Car ", car.getRoadName() + car.getNumber(), " set to Location: " , midpointLocation.toString(), ", Track: ", midpointTrack.toString())
                i += 1

        j = 0
        for engine in engineList:
            if (engine.getLocationName() == self.endpointLocation and engine.getTrackName() == self.endpointTrack):
                engine.setLocation(midpointLocation, midpointTrack)
                print("Engine ", engine.getRoadName() + engine.getNumber(), " set to Location: ", midpointLocation.toString(), ", Track: ", midpointTrack.toString())
                j += 1

        print('Cars moved:', i, 'Engines moved:', j)

    # If the location and track are OK, move the cars and engines from staging to the interchange
        carList = self.CM.getByIdList()
        engineList = self.EM.getByIdList()
        i = 0

        for car in carList:
            if (car.getLocationName() == self.midpointLocation and car.getTrackName() == self.midpointTrack):
                car.setLocation(endpointLocation, endpointTrack)
                print("Car ", car.getRoadName() + car.getNumber(), " set to Location: ", endpointLocation.toString(), ", Track: ", endpointTrack.toString())
                i += 1

        j = 0
        for engine in engineList:
            if (engine.getLocationName() == self.midpointLocation and engine.getTrackName() == self.midpointTrack):
                engine.setLocation(endpointLocation, endpointTrack)
                print("Engine ", engine.getRoadName() + engine.getNumber(), " set to Location: ", endpointLocation.toString(), ", Track: ", endpointTrack.toString())
                j += 1

        print('Cars moved: ', i, ' Engines moved: ', j)

        return False              #False means run this only once

setCars().start()
print('Done')
