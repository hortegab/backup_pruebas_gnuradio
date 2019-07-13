#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Ani
# Generated: Wed Jul  3 05:55:44 2019
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
from b_Eye_Diagram_simple import b_Eye_Diagram_simple  # grc-generated hier_block
from b_binary_bipolar_source_f import b_binary_bipolar_source_f  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from gnuradio import qtgui


class ani(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Ani")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Ani")
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

        self.settings = Qt.QSettings("GNU Radio", "ani")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.num_symbols = num_symbols = 1000
        self.Vp = Vp = 4.
        self.Sps = Sps = 8
        self.N = N = 2048

        ##################################################
        # Blocks
        ##################################################
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.b_binary_bipolar_source_f_0 = b_binary_bipolar_source_f(
            Am=1.,
            Spb=Sps,
        )
        self.b_Eye_Diagram_simple_0 = b_Eye_Diagram_simple(
            AlphaLineas=0.5,
            Delay=0,
            GrosorLineas=20,
            N_eyes=2,
            Samprate=samp_rate,
            Sps=Sps,
            Title="Eye Diagramm",
            Ymax=2,
            Ymin=-2,
        )
        self.top_grid_layout.addWidget(self.b_Eye_Diagram_simple_0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 0.4, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.b_binary_bipolar_source_f_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.b_Eye_Diagram_simple_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ani")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_Eye_Diagram_simple_0.set_Samprate(self.samp_rate)

    def get_num_symbols(self):
        return self.num_symbols

    def set_num_symbols(self, num_symbols):
        self.num_symbols = num_symbols

    def get_Vp(self):
        return self.Vp

    def set_Vp(self, Vp):
        self.Vp = Vp

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.b_binary_bipolar_source_f_0.set_Spb(self.Sps)
        self.b_Eye_Diagram_simple_0.set_Sps(self.Sps)

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N


def main(top_block_cls=ani, options=None):

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
