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
from gnuradio import blocks
from gnuradio import qtgui
from gnuradio.filter import firdes
from PyQt4 import QtGui
import sys, sip


#######################################################
# LA CLASE QUE DESCRIBE TODO EL FLUJOGRAMA
######################################################
class my_top_block(gr.top_block):        # hereda de gr.top_block
     def __init__(self):
         gr.top_block.__init__(self)     # otra vez la herencia
  
         sample_rate = 32000
         ampl = 0.1
         fftsize=2048
 
         src0 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, 350, ampl)
         src1 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, 440, ampl)
         dst = audio.sink(sample_rate, "")
         snk = qtgui.sink_c(
            fftsize, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            sample_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
        )
         self.connect(src0, (dst, 0))
         self.connect(src1, (dst, 1))
         self.connect(src1, snk)

         self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), QtGui.QWidget)
         self.pyobj.show()


#######################################################
# EL CODIGO PARA LLAMAR EL FLUJOGRAMA “my_top_block”
######################################################
my_top_block().run()