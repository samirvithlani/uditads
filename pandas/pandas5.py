import pandas as pd

df = pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8],"C":[9,10,11,12],"D":[13,14,15,16]})
#query

#df = df.query("A in [1,2] and B in [6,7]")
df = df.query("A<3")
print(df)