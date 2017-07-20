'''Instructions
When reading in world_alcohol.csv using numpy.genfromtxt():
Use the "U75" data type
Skip the first line in the dataset
Use the comma delimiter.
Assign the result to world_alcohol.
Use the print() function to display world_alcohol.
'''
import numpy
world_alcohol = numpy.genfromtxt("world_alcohol.csv", dtype="U75", skip_header=1, delimiter=",")
print(world_alcohol)
