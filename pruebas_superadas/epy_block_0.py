"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  
    """Hecho por Homero Ortega Boada"""

    def __init__(self, samp_rate=200000., Ac=1.):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='e_VCO_frec_fc',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.complex64]
        )
        self.samp_rate = samp_rate
        self.Ac = Ac
	self.L_last=0 # numero de muestas recibidas

    def work(self, input_items, output_items):
	in0=input_items[0]
	out0=output_items[0]
        L=len(in0)
	t=np.arange(L)
	t += self.L_last
	t=t/self.samp_rate
#	t=(np.arange(L)+self.L_last)/self.samp_rate
	theta=2.*np.pi*in0*t
	out0[:] = self.Ac*np.exp(1.j*theta)
	print out0	
	self.L_last += L
        return len(out0)
