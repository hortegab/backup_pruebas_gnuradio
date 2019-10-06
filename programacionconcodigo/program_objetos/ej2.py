from gnuradio import gr
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio.filter import firdes

from PyQt5 import QtGui
import sys, sip

class mi_primer_esquema(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)

        # Para que lo nuestro sea considerado una aplicacion tipo QT GUI
        self.qapp = QtGui.QApplication(sys.argv)

        samp_rate = 1e6
        fftsize = 2048

        self.src = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 0.1, 1, 0)
        self.nse = analog.noise_source_c(analog.GR_GAUSSIAN, 0.1)
        self.add = blocks.add_cc()
        self.thr = blocks.throttle(gr.sizeof_gr_complex, samp_rate, True)

        self.snk = qtgui.sink_c(
            fftsize, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
        )

        self.connect(self.src, (self.add, 0))
        self.connect(self.nse, (self.add, 1))
        self.connect(self.add, self.thr, self.snk)

        # Se establece como deseamos ver los resultados graficos
        self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), QtGui.QWidget)
        self.pyobj.show()

def main():
    tb = mi_primer_esquema()
    tb.start()
    tb.qapp.exec_()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
