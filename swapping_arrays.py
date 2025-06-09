import numpy as np
a=np.arange(12).reshape(4,3)
def swap(array, index1, index2):
    a[:,[index1,index2]]=a[:,[index2, index1]]
swap(a, 2,0)
print(a)