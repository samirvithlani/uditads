import pandas as pd
import numpy as np

#data = ['royal','techno','soft','pvt','ltd']
#data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
#data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42],'Address':['Mumbai','Pune','Bangalore','Hyderabad'],'Qualification':['Msc','Bsc','MCA','Phd']}
data = np.array([[1,2],[4,6],[7,8]])

df = pd.DataFrame(data)
print(df)