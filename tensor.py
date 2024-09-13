import numpy as np
tensor_1d = [1.3,2,4.0,23.99]
print(type(tensor_1d),tensor_1d)
#<class 'list'> [1.3, 2, 4.0, 23.99]



tensor_1d = np.array(tensor_1d)
print(type(tensor_1d),tensor_1d)
#<class 'numpy.ndarray'> [ 1.3   2.    4.   23.99]
# ndarrary 元素與元素之間是沒有逗號的

print(tensor_1d[0],tensor_1d[2]) #1.3 4.0 與list取值相同

print(tensor_1d.ndim,tensor_1d.shape,tensor_1d.dtype)
#1 (4,) float64
