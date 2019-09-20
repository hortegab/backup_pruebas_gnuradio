import numpy as np
from gnuradio import gr

class decimator(gr.decim_block):
    """Elimins paso-1 muestras, de manera que solo quedan vigentes las muestras separadas en paso muestras"""
    def __init__(self, paso=2):
        gr.decim_block.__init__(self,
            name="e_diezmad_ff",
            in_sig=[np.float32],
            out_sig=[np.float32], decim=paso)

        # variables externas
	self.paso = paso
	
    def work(self, input_items, output_items):
        # traduccion a algo que podemos manejar mejor
        in0 = input_items[0]
        out0 = output_items[0]
        # Logica principal
	out0[:] = in0[::self.paso]
        return len(output_items[0])

