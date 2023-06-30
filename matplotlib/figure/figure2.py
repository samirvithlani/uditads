import matplotlib.pyplot as plt
from matplotlib.figure import Figure


fig = plt.figure(figsize=(5,4))
ax1 = fig.add_axes([1,1,1,1])
ax2 = fig.add_axes([1,0.5,0.5,0.5])
ax1.plot([2,3,4,5,5,6,6],[5,7,1,3,4,6,8])
ax2.plot([1,2,3,4,5],[2,3,4,5,6])
plt.show()