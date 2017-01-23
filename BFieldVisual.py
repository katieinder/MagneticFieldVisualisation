'''Quiver Practice'''

#import libraries
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(10,20,11)
y=np.linspace(10,20,11)
X, Y =np.mgrid[0:11,0:11]
#increasing number of points increases number of arrows
u=10*np.cos(np.pi*X)
v=10*np.sin(np.pi*Y)
#increasing constant before increases size of arrows, i.e length
#having 1*X and 10*Y make the arrows point more in the positive direction
q=plt.quiver(X,Y,u,v, scale=100, color='m')
#decreasing scale reduces number of arrows and increases their length
#p=plt.quiverkey(q, 5,5,5,label='ex')
#don't see reason for quiver key yet

plt.show()
