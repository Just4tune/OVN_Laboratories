import numpy as np
import matplotlib.pyplot as plt


x= np.array([1,2,3,4,5])
y=np.array([2,1,4,5,8])

z=x+y

print(z)

x=np.linspace(0,10,1000)
y=np.cosh(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('cosh(x)')
plt.grid()
plt.show()
