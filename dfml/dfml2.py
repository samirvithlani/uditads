import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    'Age':[45,38,90,60,40,50,2,32,8,15,27,69,73,55]
})
plt.hist(df['Age'])
plt.show()
