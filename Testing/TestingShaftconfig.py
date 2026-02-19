class Shaft:
    def __init__(self):
        # Runs when object is created from class
        pass 

    class ForceAnalysis:
        def __init__(self, gear_type):
            self.gear_type = gear_type

    class StressAnalysis:
        pass

    class DeflectAnalysis:
        pass

force_object = Shaft().ForceAnalysis("Spur Gear")
print(force_object.gear_type)
print(type(force_object))

force_object = Shaft().ForceAnalysis("Spur Gear")
print(force_object.gear_type)
print(type(force_object))

class Parent:
    pass

class Child(Parent):
    pass

x = Child() 
print(type(x))