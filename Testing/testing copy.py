#Testing innner classes calling and structure
#Method 2 -
class OuterTesting():
    #InnerTesting = InnerTesting
    def __init__(self):
        pass
        #self.InnerTesting = InnerTesting
    
    class InnerTesting:
        def __init__(self):
            pass
        def innermethod(self):
            print("Activated innermethod")

x = OuterTesting()
x.InnerTesting().innermethod()

#Interesting...
# So in this configuration, the inner class is not an attribute of the outer class,
# but rather a separate class that can be accessed through the outer class. 
# The inner class can have its own methods and attributes, and 
# can be instantiated separately from the outer class.

