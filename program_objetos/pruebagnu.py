#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: If Else
# Generated: Thu Sep 13 11:39:57 2018
##################################################

##################################################
# LO QUE HAY QUE IMPORTAR
##################################################
from gnuradio import gr
from gnuradio import audio
from gnuradio import analog
from gnuradio import qtgui
from gnuradio.filter import firdes
import sys, sip
#from PyQt4 import QtGui
from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import qtgui
from distutils.version import StrictVersion


#######################################################
# LA CLASE QUE DESCRIBE TODO EL FLUJOGRAMA
######################################################
class top_block(gr.top_block):        # hereda de gr.top_block
     def __init__(self):
         gr.top_block.__init__(self)     # otra vez la herencia
         Qt.QWidget.__init__(self)
         self.setWindowTitle("Top Block")
         qtgui.util.check_set_qss()
         try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
         except:
             pass

        # self.qapp = QtGui.QApplication(sys.argv)
         samp_rate = 32000
         ampl = 10.
         fftsize = 2048
 
         src0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 350, ampl)
         src1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 440, ampl)
         dst = audio.sink(samp_rate, "")
         snk = qtgui.sink_f(
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
         self.connect(src0, (dst, 0))
         self.connect(src1, (dst, 1))
         self.connect(src0,snk)

        # Se establece como deseamos ver los resultados graficos
         self.snk.set_update_time(1.0/10)
         self._snk_win = sip.wrapinstance(self.snk.pyqwidget(), Qt.QWidget)
         self.top_layout.addWidget(self._snk_win)
         self.snk.enable_rf_freq(False)
#######################################################
# EL CÓDIGO PARA LLAMAR EL FLUJOGRAMA “my_top_block”
######################################################
def main(top_block_cls=top_block, options=None):

     if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
         style = gr.prefs().get_string('qtgui', 'style', 'raster')
         Qt.QApplication.setGraphicsSystem(style)
     qapp = Qt.QApplication(sys.argv)

     tb = top_block_cls()
     tb.start()
     tb.show()

     def quitting():
         tb.stop()
         tb.wait()
     qapp.aboutToQuit.connect(quitting)
     qapp.exec_()


if __name__ == '__main__':
     main()
