import matplotlib.pyplot as plt
x=[]
y=[]
# y=x2+3
for i in range(-100,101):
    x.append(i)
    y.append(i**2+3)



plt.plot(x, y)
plt.plot(0,0,marker='o',markersize=5,color='red')
plt.show()