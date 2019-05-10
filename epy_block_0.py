import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """calculate the mean of a staocastic process that comes as a signal. it is considered that every new frame of N samples is a new sample function of the process"""

    def __init__(self, N=128, Nensayos=1000): 


        gr.sync_block.__init__(
            self,
            name='e_stoc_proc_mean_ff',   # will show up in GRC
            in_sig=[(np.float32, N)],
            out_sig=[(np.float32, N)]
        )
        self.N = N
        self.Nensayos = Nensayos
        self.med=np.empty(N,dtype=np.float32)
#        self.med=np.zeros(N)
        self.count=np.uint64=0

    def work(self, input_items, output_items):
        in0 = input_items[0][0, :]
        out0=output_items[0]
        if self.count < self.Nensayos:
            self.count += 1	
        self.med = self.med*(self.count-1)/self.count+in0/self.count
        out0[:]=self.med
        return len(out0)
