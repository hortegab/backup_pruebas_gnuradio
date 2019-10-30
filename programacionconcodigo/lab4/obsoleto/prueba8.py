import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np



def makeFig(i):
    t = np.arange(0,2, 0.01)
    s=np.random.rand(200)
    ax1.clear()
    ax1.plot(t, s)

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
ani=animation.FuncAnimation(fig,makeFig,interval=1)
plt.show()
