import matplotlib.pyplot as plt
from matplotlib.figure import Figure

x = [3,1,3]
y =[3,2,1]

fig = plt.figure(figsize=(5,4))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
#ax.set_xlim(1,3)
ax.set_ylim(1,2)
ax.plot(x,y)


plt.show()