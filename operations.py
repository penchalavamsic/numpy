import numpy as np
a="HELLO WORLD"
c=np.fromiter(a, dtype='U2')#fromiter
b=np.arange(1,20,2, dtype=int) #arange
print(b)
print(c)
d=np.ones([4,2])#ones
e=np.empty([3,3])#empty
print(d,e)