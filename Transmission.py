import Inputs
import Shaft
import Bearings
import Gears

#no need to import user_input nor catalog data IF this function is going to
#actually be used inside a main.py where the process is actually run

class Transmission:
    Shaft = Shaft # Innername = ImportedClass
    Bearings = Bearings
    Gears = Gears
    # These are now 

    def __init__(self,user_input:Inputs, catalog_data):
        # P: Maybe assign all the necessary catalog data values
        # to their rightfull class, here
        # The functions are run in the main, usign like Transmission.Shaft(value)
        # Verify
        self.user_input = user_input
        self.catalog_data = catalog_data
        self.dfd
        #self.gears = Gears(###) #Example of structure
        #self.shaft = Shaft(###)
        #self.bearings = Bearings(###)