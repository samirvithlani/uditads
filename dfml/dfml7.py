import matplotlib.pyplot as plt
import random

date = [i for i in range(2000, 2021)]
value =[]
for i in range(21):
    value.append(random.randint(100, 1000))

fig,ax = plt.subplots(figsize=(10,6))
ax.scatter(date,value)
ax.axvspan(2006,2010,color='green',alpha=0.2)
plt.show()