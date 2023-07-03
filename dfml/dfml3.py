import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'Object':["phone","charger","cable","dock","box","others"],
    'Price':[12000,4000,2000,1500,500,2500]
})
plt.pie(df["Price"],labels=df["Object"])
plt.show()