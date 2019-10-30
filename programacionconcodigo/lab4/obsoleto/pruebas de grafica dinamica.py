import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *
plt.ion()

contador=0
tamano=4

def migrafiquita():
    global contador, tamano
    if contador < tamano:
        t = np.arange(0,2, 0.01)
        s=np.random.rand(200)
        plt.plot(t, s)
        plt.pause(0.01)
        contador += 1
    #print("madre", contador, tamano)  
    else:
        contador=0
        plt.clf()
        
while True:
    migrafiquita()
#migrafiquita()
