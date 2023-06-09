import pandas as pd

data = pd.read_csv('D:\\royal\\udita-ds\\pandas\\data.csv',index_col = 'Name')
#show particular column
# data = data['Age']
# first = data.loc['Ralf']
# second = data.loc['Nev']
# print(first," \n\n",second)
# print(data)
x = data.head(2)
y = data.tail(2)
print(x)
print(y)

