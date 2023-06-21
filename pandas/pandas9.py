import pandas as pd
import numpy as np

data =pd.read_csv("D:\\royal\\udita-ds\\pandas\\ipl.csv")
print(data)

#data.... pandas...
ser = pd.notnull(data["Name"])
print(ser)