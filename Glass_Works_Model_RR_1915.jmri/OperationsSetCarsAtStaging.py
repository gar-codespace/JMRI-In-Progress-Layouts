# Author: Daniel Boudreau, copyright 2011
#
# Modified by Greg Ritacco November 2015

import jmri

class setCars(jmri.jmrit.automat.AbstractAutomaton):
  def init(self):

    # change the locationName entry to the name of your staging location
    self.locationName1 = "Salem1"
    self.locationName2 = "Salem"
    # change the trackName entry to the staging track all cars go to
    self.trackName = "Yard"

    return

  def handle(self):

    # check the location and track
    lm = jmri.jmrit.operations.locations.LocationManager.instance()
    testLocation = lm.getLocationByName(self.locationName1)
    testTrack = testLocation.getTrackByName(self.trackName, None)

    if (testLocation == None):
      print "Location (", self.locationName1, ") does not exist"
      return False		# done error!
    else:
      print "Location (", self.locationName1, ") is a valid location."

    if (testTrack == None):
      print "Track (", trackName, ") does not exist at location (", self.locationName1, ")"
      return False		# done error!
    else:
      print "Track (", self.trackName, ") is a valid track."

    # get the car manager
    cm = jmri.jmrit.operations.rollingstock.cars.CarManager.instance()
    # get a list of cars from the manager
    carList = cm.getByIdList()

    print "Setting all cars at", self.locationName2, "to Location:", self.locationName1, "Track:", self.trackName
    i = 0

    # set all the cars at staging to the same track
    for car in carList:
      # print "Car", car.getTypeName(), car.getLocationName(), car.getTrackName()
      if (car.getLocationName() == self.locationName2):
        car.setLocation(testLocation, testTrack)
        i = i + 1
        print "Car", car.getRoadName(), car.getNumber(), "set to Location:", car.getLocationName(),", Track:", car.getTrackName()

    print i, "cars were set."

    return False              # all done, don't repeat again

setCars().start()          # create one of these, and start it running
