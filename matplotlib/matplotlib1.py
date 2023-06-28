from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1,11)
y = 2 * x + 5
print(x)
print(y)

plt.bar(x,y)
plt.show()