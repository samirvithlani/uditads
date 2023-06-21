import pandas as pd
import numpy as np

#data =pd.read_csv("D:\\royal\\udita-ds\\pandas\\ipl.csv")
np.random.seed(25)
data = pd.DataFrame(np.random.randn(10,3),columns=["A","B","C"])
#print(data)
#data.iloc[-1] = np.nan
#data = data.add(10)
#data = data.add(10,fill_value=10)


#sub....
#series..convert...
#data = data.sub(10,axis=1)

#mul
#div

print(data)
#insert row
#ata.loc[2] = ["amit","mi","bowler"]
#data.insert(3,"ok","any")
# data.add(1)
# data.add("ok",fill_value=0)
# print(data)
