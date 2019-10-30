import numpy as np
from gnuradio import gr


class e_vector_fft_ff(gr.sync_block):
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, N=128):  
        gr.sync_block.__init__(
            self,
            name='e_vector_fft_ff',   
            in_sig=[(np.float32,N)],
            out_sig=[(np.float32,N)]
        )
        self.N = N

    def work(self, input_items, output_items):
        in0 = input_items[0]
    	out0 = output_items[0]
	out0[:]=abs(np.fft.fftshift(np.fft.fft(in0,self.N),1)) 
        return len(output_items[0])
