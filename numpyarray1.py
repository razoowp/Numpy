import numpy as np

#One Dimensional Array - Vector
a = np.array([1,2,3])
print(a)
print(a.shape)
'''
output:
[1,2,3]
(3,)
'''

#Two Dimensional Array - Matrix
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape)
'''
[[1 2 3]
 [4 5 6]]
 (2,3)
'''
#we can also use () tuple in inner lists. 
c = np.array([(1,2,3),(4,5,6)])
print(c)
print(c.shape)
'''
[[1 2 3]
 [4 5 6]]
(2, 3)
'''