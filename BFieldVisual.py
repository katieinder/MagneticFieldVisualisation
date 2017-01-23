'''Quiver Practice'''

#import libraries
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,11)
y=np.linspace(0,10,11)
X, Y =np.mgrid[0:11,0:11]
u=5*X
v=5*Y
q=plt.quiver(X,Y,u,v,angles='xy', scale=1000, color='r')
p=plt.quiverkey(q, 1,16.5,50, label="50m/s", coordinates='data', color='r')
plt.show()
