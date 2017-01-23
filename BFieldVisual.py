'''Quiver Practice'''

#import libraries
import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(0,10,11)
y=np.linspace(0,10,11)
X, Y =np.mgrid[0:10,0:10]
#increasing number of points increases number of arrows
u=10*X
v=10*Y
#increasing constant before increases size of arrows, i.e length
#having 1*X and 10*Y make the arrows point more in the positive direction
q=plt.quiver(X,Y,u,v, scale=1000, color='m')
#decreasing scale reduces number of arrows and increases their length
#p=plt.quiverkey(q, 1,16.5,50,label='ex')
#don't see reason for quiver key yet

plt.show()
