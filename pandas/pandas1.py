import pandas as pd
import numpy as np
#data = np.array(['a','b','c','d'])
#data = np.zeros(5, dtype=int)
data = np.array([[1,2,3],[4,5,6]])
#data = np.full(5, 60, dtype=float)
ser = pd.Series(data)
print(ser)

