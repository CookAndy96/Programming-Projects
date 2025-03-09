import numpy as np

"""What are classes?"""

class Name:                                 # Define name of class
    def __init__(self, data1, data2):       # Initialisation function. This is where all of the data for the class will go
        self.data1 = data1
        self.data2 = data2

# Example class

class Pets:
    def __init__(self, animal):
        self.animal = animal

anim = Pets('dog')

print(anim.animal)  # Prints 'dog'

# What more can we do with classes

