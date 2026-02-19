import #abstract class library as ABC

# Gear from user data? for now. How to make scalable for future
# Later it would be a decision from the ai, how to make scalable

# What type of information is necessary of the gears?
# - Gear type
# - Gear amount
# -
# -
# (Also, what needs to be found out)
# - Pitch or whatever

class Gears: 
    def __init__ (self, user_input_gear_type):
        self.gear_type = user_input_gear_type
        #self.gear_amount =
        #

    # Make all method outputs store to the class attributes, makes for easy programming and structure.
        # Runs when object is created from class
        pass

# abstract methods i believe
# abstract attribute of gear_type also rewritten
# Helical subclass
# Spur gear subclass

class Spur_Gears(Gears):
    def __init__(self, user_input_gear_type):

# subclasses and Inner classes are NOT the same thing