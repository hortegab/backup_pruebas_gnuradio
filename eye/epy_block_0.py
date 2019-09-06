import numpy as np
from gnuradio import gr
import matplotlib.pyplot as plt

class blk(gr.sync_block):
    def __init__(self, factor=1.0):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='scope_interno',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.factor = factor

    def work(self, input_items, output_items):
        output_items[0][:] = input_items[0] * self.factor
        y=output_items[0]
        plt.plot(output_items[0])
        plt.ylabel('some numbers')
        plt.show()

        return len(output_items[0])

