import pandas as pd

data =pd.read_csv("D:\\royal\\udita-ds\\pandas\\data2.csv")
data.dropna(inplace=True)
#data["Team"] = data["Team"].str.split("S")
#data["Team"] = data["Team"].str.join(",")
data["Name"] = data["Name"].str.upper()
data["Name"] = data["Name"].str.replace("A","@")

print(data)

