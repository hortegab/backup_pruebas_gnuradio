#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.9.0.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import numpy as np



from gnuradio import qtgui

class prueb2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "prueb2")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.N = N = 4
        self.Dz = Dz = 0.5
        self.theta_i_gr = theta_i_gr = 90
        self.distancias = distancias = Dz*np.array(range(N))
        self.w = w = [1,1,1,1]
        self.samp_rate = samp_rate = 32000
        self.fases = fases = -2*np.pi*distancias*np.cos(theta_i_gr*np.pi/180)
        self.Resol_angular_gr = Resol_angular_gr = 1

        ##################################################
        # Blocks
        ##################################################
        self._theta_i_gr_range = Range(0, 360, Resol_angular_gr, 90, 200)
        self._theta_i_gr_win = RangeWidget(self._theta_i_gr_range, self.set_theta_i_gr, 'theta_i_gr', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._theta_i_gr_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("Campo E")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0.set_min(i, -N)
            self.qtgui_number_sink_0.set_max(i, N)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_const_source_x_0_1 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, w[2]*np.exp(1j*fases[2]))
        self.analog_const_source_x_0_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, w[3]*np.exp(1j*fases[3]))
        self.analog_const_source_x_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, w[1]*np.exp(1j*fases[1]))
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, w[0]*np.exp(1j*fases[0]))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.analog_const_source_x_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_number_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "prueb2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N
        self.set_distancias(self.Dz*np.array(range(self.N)))

    def get_Dz(self):
        return self.Dz

    def set_Dz(self, Dz):
        self.Dz = Dz
        self.set_distancias(self.Dz*np.array(range(self.N)))

    def get_theta_i_gr(self):
        return self.theta_i_gr

    def set_theta_i_gr(self, theta_i_gr):
        self.theta_i_gr = theta_i_gr
        self.set_fases(-2*np.pi*self.distancias*np.cos(self.theta_i_gr*np.pi/180))

    def get_distancias(self):
        return self.distancias

    def set_distancias(self, distancias):
        self.distancias = distancias
        self.set_fases(-2*np.pi*self.distancias*np.cos(self.theta_i_gr*np.pi/180))

    def get_w(self):
        return self.w

    def set_w(self, w):
        self.w = w
        self.analog_const_source_x_0.set_offset(self.w[0]*np.exp(1j*self.fases[0]))
        self.analog_const_source_x_0_0.set_offset(self.w[1]*np.exp(1j*self.fases[1]))
        self.analog_const_source_x_0_0_0.set_offset(self.w[3]*np.exp(1j*self.fases[3]))
        self.analog_const_source_x_0_1.set_offset(self.w[2]*np.exp(1j*self.fases[2]))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_fases(self):
        return self.fases

    def set_fases(self, fases):
        self.fases = fases
        self.analog_const_source_x_0.set_offset(self.w[0]*np.exp(1j*self.fases[0]))
        self.analog_const_source_x_0_0.set_offset(self.w[1]*np.exp(1j*self.fases[1]))
        self.analog_const_source_x_0_0_0.set_offset(self.w[3]*np.exp(1j*self.fases[3]))
        self.analog_const_source_x_0_1.set_offset(self.w[2]*np.exp(1j*self.fases[2]))

    def get_Resol_angular_gr(self):
        return self.Resol_angular_gr

    def set_Resol_angular_gr(self, Resol_angular_gr):
        self.Resol_angular_gr = Resol_angular_gr




def main(top_block_cls=prueb2, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
