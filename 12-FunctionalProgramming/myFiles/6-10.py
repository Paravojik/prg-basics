
import matplotlib.pyplot as plt
import numpy as np


cities={"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

x=np.array(list(map(lambda x:x,cities)))
y=np.array(list(map(lambda x:cities[x],cities)))
print(x,y)

plt.title("City Temperatures")
plt.xlabel("Cities")
plt.ylabel("Temperature in C")


plt.bar(x,y)
plt.show()