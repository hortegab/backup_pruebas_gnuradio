#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Oct 10 21:29:38 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from b_PSD import b_PSD  # grc-generated hier_block
from b_PSD_c import b_PSD_c  # grc-generated hier_block
from b_binary_bipolar_source_f import b_binary_bipolar_source_f  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.Sps = Sps = 8

        ##################################################
        # Blocks
        ##################################################
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(Sps, (([1.]*Sps)))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.b_binary_bipolar_source_f_0 = b_binary_bipolar_source_f(
            Am=1.,
            Spb=1,
        )
        self.b_PSD_c_0 = b_PSD_c(
            Ensayos=1000000,
            Fc=0.,
            N=1024,
            Titulo='hola',
            Ymax=6e-6,
            samp_rate_audio=samp_rate,
        )
        self.top_grid_layout.addWidget(self.b_PSD_c_0)
        self.b_PSD_0 = b_PSD(
            Ensayos=1000000,
            N=1024,
            Titulo='espectro',
            Ymax=5e-6,
            samp_rate=samp_rate*Sps,
        )
        self.top_grid_layout.addWidget(self.b_PSD_0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.b_binary_bipolar_source_f_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.b_PSD_c_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.b_PSD_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_float_to_complex_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_PSD_c_0.set_samp_rate_audio(self.samp_rate)
        self.b_PSD_0.set_samp_rate(self.samp_rate*self.Sps)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.interp_fir_filter_xxx_0.set_taps((([1.]*self.Sps)))
        self.b_PSD_0.set_samp_rate(self.samp_rate*self.Sps)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
