#Testing inner classes calling and structure
#Method 1
class InnerTesting:
    def __init__(self):
        pass
    def innermethod(self):
        print("Activated innermethod")

class OuterTesting:
    #InnerTesting = InnerTesting
    def __init__(self):
        self.InnerTesting = InnerTesting #Remember to put () for it to be a class object

X = OuterTesting()
x = X.InnerTesting() # the "()" go on the method, since this is an attribute technically
# Instance of InnerTesting, created from attribute of OuterTesting class
print(type(X))
print(type(x))
x.innermethod()

# ---WHAT I LEARNED---
# self.InnerTesting = InnerTesting - This sets a class creatior of objects as an attributek, when you 
# put () at the end, you are creating a specific class object instance, aka, an object already
# when you don't, though, you are able to use that attribute to CREATE object instances, so that
# x = X.InnerTesting() is correct, and you could put variables inside here, instead of having to put them in the init as direct inputs to a InnerTesting(inputs) thing.


#In this method, it would be required to have the class defined beforehand, OUTSIDE of the outer class
# Where you set it as an attrbute of the outer class

# Q: why does this allow me to put a class without the ()
# A: This just creates a class object, not an instance (???)
# Explanation:
# self.InnerTesting = InnerTesting -> x.InnerTesting is the class. You can create instances later with x.InnerTesting().
# self.InnerTesting = InnerTesting() -> x.InnerTesting is an instance. Call methods directly with x.InnerTesting.innermethod(); x.InnerTesting() will raise TypeError because the instance isn't callable.







