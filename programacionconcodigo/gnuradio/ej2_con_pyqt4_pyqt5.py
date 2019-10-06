# La libreria obligatoria
from gnuradio import gr
from gnuradio import qtgui
# Las librerias que dependen de lo que vamos a usar
from gnuradio import blocks
from gnuradio import analog
from gnuradio.filter import firdes

# Las librerias que ayudan a graficar

from PyQt4 import QtGui as Qt # Si se requiere PyQt5 reemplace por: from PyQt5 import Qt
import sys, sip

class flujograma(gr.top_block):
    def __init__(self):

        # para heredar completamente los recursos para crear un flujograma
        gr.top_block.__init__(self)

        # Para que lo nuestro sea considerado una aplicación tipo QT GUI
        self.qapp = Qt.QApplication(sys.argv)

        # Las variables para el flujograma
        samp_rate = 1e6
        fftsize = 2048

        # los bloques del Flujograma
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

        # Las conecciones de los bloques
        self.connect(self.src, (self.add, 0))
        self.connect(self.nse, (self.add, 1))
        self.connect(self.add, self.thr, self.snk)

        # Se establece como deseamos ver los resultados graficos
        self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), Qt.QWidget)
        self.pyobj.show()

def main():
    simulador_de_la_envolvente_compleja = flujograma()
    simulador_de_la_envolvente_compleja.start()
    simulador_de_la_envolvente_compleja.qapp.exec_()