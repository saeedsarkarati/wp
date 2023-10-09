import numpy as np
a = np.ones([10])
for i in range (len(a)):
	a[i] = i
a *= 2
a[a>10]*= -1
b = a[3:]
print (a)
a[9] = 1000
print (b)
