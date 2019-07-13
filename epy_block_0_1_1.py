"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
from eyediagram.demo_data import demo_data
from eyediagram.mpl import eyediagram
import matplotlib.pyplot as plt

import matplotlib.animation as animation
from matplotlib import style
import pylab



class blk(gr.sync_block):  
    """hecho por: Homero Ortega Boada. Permite obtener el diagrama de ojo"""

    def __init__(self, Sps=8, N=2048):
        gr.sync_block.__init__(self, name='Eye Diagram_v5', in_sig=[(np.float32, N)], out_sig=None)
        self.Sps = Sps
	self.N = N
	self.D=0
#	pylab.ion()
    def makeFig(self):
	eyediagram(self.D, 2*self.Sps, offset=int(self.Sps/2), cmap=plt.cm.coolwarm)
	#plt.show()
	
	pylab.show()   

    def work(self, input_items, output_items):
  	in0 = input_items[0] # in0 es un 2D array (como una matrix)
	self.D=in0.reshape(-1)/(in0.max()*2.)
	self.makeFig()
        return len(input_items[0])
