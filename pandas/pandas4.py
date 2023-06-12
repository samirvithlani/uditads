import pandas as pd

data = [
    ["India",2001,200000,'Asia'],
    ["Austrelia",1995,45678,'Australia'],
    ['Brazil',2000,56789,'America'],
    ['China',1962,345670,'Asia'],
    ['France',2001,67000,'Europe'],
    ['Usa',2000,23456,'America'],
    ['UK',2001,23456,'Europe']]

df = pd.DataFrame(data,columns=['Country','Year','Population','Continent'])


#sort by country....
#df = df.sort_values(by=['Country'])
#df = df.sort_values(by=["Population"],ascending=False)
#df = df.sort_values(by =["Population"],na_position='first')
df = df.sort_values(by =["Population","Year"],ascending=[True,False])
print(df)

