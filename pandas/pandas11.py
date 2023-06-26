import pandas as pd

data =pd.read_csv("D:\\royal\\udita-ds\\pandas\\data2.csv")
#data.sort_values("Name",inplace=True,kind="mergesort",axis=0)
#print(data)

# bool_series = data["Name"].duplicated()
# # data.head()
# data[bool_series]
# print(data[bool_series])

#bool_series = data["Name"].str.startswith("o")
#and operator
bool_series = data["Name"].str.startswith("o") & (data["Age"]>55)
#bool_series = data["Age"]>55
print(data[bool_series])