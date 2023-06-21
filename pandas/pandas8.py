import pandas as pd
import numpy as np

data =pd.read_csv("D:\\royal\\udita-ds\\pandas\\ipl.csv")
print(data)
teams = data["Name"].unique()
cnt = data["Name"].nunique()
col = data.columns
nullcheck = data.isnull()
print("......",nullcheck)
print(col)
print(cnt)
print(teams)
