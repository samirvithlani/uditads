import matplotlib.pyplot as plt
from matplotlib.figure import Figure

x = [3,1,3]
y =[3,2,1]
z = [1,3,1]

plt.figure(figsize=(5,4))
plt.subplot(1,2,1)
plt.plot(x,y)

plt.subplot(122)
plt.plot(z,y)