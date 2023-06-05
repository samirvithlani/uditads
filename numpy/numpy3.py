import numpy as np
arr = np.array([[-1,2,0,4,1,7],[4,0.5,6,0,9,8],[2.5,0,7,8,9,0],[8,0,3,-7,4,2]])
#temp = arr[:2,::2]
#temp =arr[[0,1,2,3],[3,2,1,0]]
cond = arr>10
print(cond)



#arr = np.arange(1,10).reshape(3,3)
#print(arr)
#temp = arr[:4,::3]
#print(temp)