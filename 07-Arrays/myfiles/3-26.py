import matplotlib.pyplot as plt
import math
x=[]
y=[]
for i in range(361):
    x.append(i)
    y.append(math.sin(math.radians(i)))

plt.plot(x, y)
plt.plot([0,360],[0,0],color='red',linestyle='--')
plt.show()