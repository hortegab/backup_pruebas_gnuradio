"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.decim_block):  # other base classes are basic_block, decim_block, interp_block
    """Este bloque realiza un diezmado asi: cada Sps muestras solo pasa una"""

    def __init__(self, Sps=8):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.decim_block.__init__(
            self,
            name='e_diezmador_cc',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64], decim = Sps
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.Sps = Sps

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        in0 = input_items[0]
        out = output_items[0]
        out[:] = in0[::self.Sps]
        return len(output_items[0])
