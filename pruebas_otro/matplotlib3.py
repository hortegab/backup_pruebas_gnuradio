import matplotlib.pyplot as plt
import numpy as np
#from mod import plotsomefunction
#from diffrentmod import plotsomeotherfunction

def plotsomefunction(ax, x):

    return ax.plot(x, np.sin(x))

def plotsomeotherfunction(ax, x):

    return ax.plot(x,np.cos(x))


fig, ax = plt.subplots(1,1)
x = np.linspace(0,np.pi,1000)
l1 = plotsomefunction(ax, x)
l2 = plotsomeotherfunction(ax, x)
plt.show()
