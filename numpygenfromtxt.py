'''
    Read in data sets using the numpy.genfromtxt() function.

    Use the numpy.genfromtxt() function to read "world_alcohol.csv" into a NumPy array named world_alcohol.
    Use the type() and print() functions to display the type for world_alcohol.
'''

import numpy
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",")
print(type(world_alcohol))


'''
output:
<class 'numpy.ndarray'>

'''
