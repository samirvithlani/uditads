import matplotlib.pyplot as plt
from matplotlib.figure import Figure

fig = plt.figure(figsize=(8,8))

ax = fig.add_axes([1,1,1,1])
ax.plot([2,3,4,5,5,6,6],[5,7,1,3,4,6,8])
plt.show()
