# import specific input object instance
# import specific CatalogData object instance
# Or these will be input in the main.py that runs, and the classes only
from Shaft.py import Shaft
from Bearings.py import Bearings
from Gears.py import Gears

class Transmission(user_input,catalog_data):
    #Shaft = Shaft
    #Bearings = Bearings
    #Gears = Gears

    def __init__(self):
        self.dfd
        self.dfd
        self.dfdf

        class ForceAnalysis(): #Which one to use
            pass
        
        class Bearing():
            pass

        class Shaft():
            def __init__(self):
                # Runs when object is created from class
                pass 

            class ForceAnalysis(): 
                pass

            class StressAnalysis():
                pass

            class DeflectAnalysis():
                pass

        #subclass Force analysis (Are there 2 force analysis or just this one)
        #subclass stress analysis
        #subclass deflection analysis

        # Subclasses (children?) or methods?
        #Clases makes the most sense since easier to set atributes to values to access
        # but if we are going to use struct, does this even matter?

        # ***
        # I think it makes the most sense to make the Shaft class a child of Force analysis, stress analysis, etc,
        # ***

# ------------
# Multi Inner Class structure makes sense here, but has to be acessed
# by atributes, it seems
# https://www.w3schools.com/python/python_class_inner.asp
# ------------