import pandas as pd

data = pd.read_csv("D:\\royal\\udita-ds\\pandas\\data2.csv")

filter1 = data["Name"]=="raj"
filter2 = data["Age"]>50

data.where(filter1 | filter2,inplace=True)
print(data)