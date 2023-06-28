from matplotlib import pyplot as plt
x = [6,8,10]
y = [6,16,6]

x2 = [6,9,11]
y2 = [6,15,7]


plt.bar(x,y,align='center')
plt.bar(x2,y2,color='g',align='center')
plt.show()
