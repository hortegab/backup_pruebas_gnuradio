
import numpy as np
from gnuradio import gr


class e_add_cc(gr.sync_block):  
    """e-ddd blok. Hace lo mismo que add solo que es un embebido creado para propositos pedagogicos"""

    def __init__(self):
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='e_dd_ff',   # will show up in GRC
            in_sig=[np.complex64,np.complex64],
            out_sig=[np.complex64]
        )
        
    def work(self, input_items, output_items):
	in0 = input_items[0]
	in1 = input_items[1]
	out0 = output_items[0]
	out0[:]=in0+in1
        return len(out0)
