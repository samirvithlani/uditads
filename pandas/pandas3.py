import pandas as pd

data = pd.read_csv('D:\\royal\\udita-ds\\pandas\\data.csv',index_col = 'Name')
#show particular column
data = data['Age']
print(data)