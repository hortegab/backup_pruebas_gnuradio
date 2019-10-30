import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *
plt.ion()

def makeFig():
    t = np.arange(0,2, 0.01)
    s=np.random.rand(200)
    plt.plot(t, s)
    plt.pause(0.01)

while True:
    makeFig()
