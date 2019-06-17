import numpy as np
from gnuradio import gr
from eyediagram.demo_data import demo_data
from eyediagram.mpl import eyediagram
import matplotlib.pyplot as plt

import matplotlib.animation as animation
from matplotlib import style
style.use('fivethirtyeight')



def animate(i):
    graph_data = open('example.txt', 'r').read()
    lines=graph_data.split('\n')

    for line in lines:
        if len(line)> 1:
	    x,y = line.split(',')
	    self.xs.append(x)
	    self.ys.append(y)


class blk(gr.sync_block):  
    """hecho por: Homero Ortega Boada. Permite obtener el diagrama de ojo"""

    def __init__(self, Sps=8):
        gr.sync_block.__init__(self, name='animacion2', in_sig=[np.float32], out_sig=None)
        self.Sps = Sps
	#self.N = N
	self.xs= []
	self.ys= []

    def work(self, input_items, output_items):
  	in0 = input_items[0] # in0 es un 2D array (como una matrix)
	y=in0.reshape(-1)    # Esto traduce el 2D array a 1D array (a un vector)
	y=y/(y.max()*2.)     # Esto normaliza los valores de y
	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1)
	ani = animation.FuncAnimation(fig, animate, interval=1000)
	ax1.clear()
	ax1.plot(self.xs,self.ys)
	plt.show()
        return len(input_items[0])
