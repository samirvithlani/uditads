import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'X':[2001,2002,2003,2004,2005],
    'Y':[2,4,6,10,15]
})

plt.plot(df['X'],df['Y'])
plt.show()

plt.scatter(df['X'],df['Y'])
plt.show()