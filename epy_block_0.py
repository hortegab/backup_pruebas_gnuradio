"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  
    """Done by Homero Ortega Boada"""

    def __init__(self, samp_rate=200000., Ac=1.):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='e_VCO_frec_fc',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.complex64]
        )
        self.samp_rate = float(samp_rate)
        self.Ac = Ac
	self.last_t=0.

    def work(self, input_items, output_items):
	in0=input_items[0]
	out0=output_items[0]
        L=len(in0)
	t=np.arange(L)/self.samp_rate+self.last_t
	theta=2.*np.pi*in0*t
	out0[:] = self.Ac*np.exp(1.j*theta)
	self.last_t += L/self.samp_rate
	return len(out0)
