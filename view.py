import numpy as np
a=np.array([1,2,5])
b=a.view()
print(id(a))
print(id(b))
b[0]=3
print(a)