import numpy as np
arr =np.array([[1,5,7],[4,7,2],[3,4,9]])

print(arr.sum())
print(arr.sum(axis=0))
print(arr.sum(axis=1))

print(arr.min())
print(arr.min(axis=0))
print(arr.min(axis=1))

print(arr.max())
print(arr.max(axis=0))
print(arr.max(axis=1))