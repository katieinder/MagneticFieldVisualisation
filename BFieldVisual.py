'''Quiver in pygame'''

#import libraries
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import pygame

pygame.init()

size=[800,600]
screen=pygame.display.set_mode(size)
pygame.display.set_caption('quiver experiment')

clock=pygame.time.Clock()

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    x = np.linspace(10, 20, 11)
    y = np.linspace(10, 20, 11)
    X, Y = np.mgrid[10:20, 10:20]
    u = 10 * X
    v = 10 * Y
    q = plt.quiver(X, Y, u, v, scale=1000, color='m')


    pygame.display.flip()
    clock.tick(60)

