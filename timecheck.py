from numpy import arange
from timeit import Timer

Nelements = 10000
Ntimeits = 10000

x = arange(Nelements)
y = range(Nelements)

t_numpy = Timer("x.sum()", "from __main__ import x")
t_list = Timer("sum(y)", "from __main__ import y")
print ("numpy: %.3e" % (t_numpy.timeit(Ntimeits)/Ntimeits,))
print ("list:  %.3e" % (t_list.timeit(Ntimeits)/Ntimeits,))
