class Shaft():
    def __init__(self):
        # Runs when object is created from class
        pass 

#subclass Force analysis
#subclass stress analysis
#subclass deflection analysis

# Subclasses (children?) or methods?
#Clases makes the most sense since easier to set atributes to values to access
# but if we are going to use struct, does this even matter?

# ***
# I think it makes the most sense to make the Shaft class a child of Force analysis, stress analysis, etc,
# ***