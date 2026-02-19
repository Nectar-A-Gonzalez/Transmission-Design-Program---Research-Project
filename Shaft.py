class Shaft:
    def __init__(self, gears:Gears):
        self.gears = gears
        # Runs when object is created from class
        pass 

    class ForceAnalysis:
        def __init__(self, gear_type):
            self.gear_type = gear_type
        
        pass

    class StressAnalysis:
        pass

    class DeflectAnalysis:
        pass

#How this would be called:
# Shaft.

# NOTE - Subclasses and Inner classes are NOT the same thing, btw.
#subclass Force analysis (Are there 2 force analysis or just this one)
#subclass stress analysis
#subclass deflection analysis

# Subclasses (children?) or methods?
#Clases makes the most sense since easier to set atributes to values to access
# but if we are going to use struct, does this even matter?

#Lets add doc descriptions

# should these be methods or attributes??