#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Aug 26 06:04:37 2019
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
from b_BERTool import b_BERTool  # grc-generated hier_block
from b_u_M_PAM_bb import b_u_M_PAM_bb  # grc-generated hier_block
from b_u_de_M_PAM_bb import b_u_de_M_PAM_bb  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import e_VCO_fase_fc_0
import e_c_p
import e_mpam_ph
import e_phase
import math
import numpy
import sip
import wform  # embedded python module
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
        self.M2 = M2 = 16
        self.Rb2 = Rb2 = 32000
        self.BpS2 = BpS2 = int(math.log(M2,2))
        self.samp_rate = samp_rate = 32000
        self.run_stop = run_stop = True
        self.Rs2 = Rs2 = Rb2/BpS2
        self.N_snr = N_snr = 64
        self.EsN0min = EsN0min = 0.
        self.EsN0max = EsN0max = 20.

        ##################################################
        # Blocks
        ##################################################
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            N_snr,
            EsN0min,
            (EsN0max-EsN0min)/float(N_snr),
            "Es/No [dB]",
            "logPe",
            "Curva de SER",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-5, 0)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(True)
        self.qtgui_vector_sink_f_0.set_x_axis_units("dB")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ["16-PSK", "QPSK", "8PSK", "BPSK", '',
                  '', '', '', '', '']
        widths = [6, 6, 6, 6, 1,
                  1, 1, 1, 1, 1]
        colors = ["magenta", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.e_phase = e_phase.blk(M=M2)
        self.e_mpam_ph = e_mpam_ph.blk(M=M2)
        self.e_c_p = e_c_p.blk(M=M2)
        self.e_VCO_fase_fc_0 = e_VCO_fase_fc_0.blk()
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_char*1, 0)
        self.b_u_de_M_PAM_bb_0 = b_u_de_M_PAM_bb(
            M=M2,
        )
        self.b_u_M_PAM_bb_0 = b_u_M_PAM_bb(
            M=M2,
        )
        self.b_BERTool_0_0_0 = b_BERTool(
            EsN0max=EsN0max,
            EsN0min=EsN0min,
            N_snr=N_snr,
            Rs=Rs2,
        )
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, 1000000)), True)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1.)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.e_VCO_fase_fc_0, 1))
        self.connect((self.analog_random_source_x_0, 0), (self.b_u_M_PAM_bb_0, 0))
        self.connect((self.b_BERTool_0_0_0, 0), (self.e_c_p, 0))
        self.connect((self.b_BERTool_0_0_0, 1), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.b_u_M_PAM_bb_0, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.b_u_M_PAM_bb_0, 0), (self.e_mpam_ph, 0))
        self.connect((self.b_u_de_M_PAM_bb_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_delay_0_1, 0), (self.b_BERTool_0_0_0, 1))
        self.connect((self.e_VCO_fase_fc_0, 0), (self.b_BERTool_0_0_0, 0))
        self.connect((self.e_c_p, 0), (self.e_phase, 0))
        self.connect((self.e_mpam_ph, 0), (self.e_VCO_fase_fc_0, 0))
        self.connect((self.e_phase, 0), (self.b_BERTool_0_0_0, 2))
        self.connect((self.e_phase, 0), (self.b_u_de_M_PAM_bb_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_M2(self):
        return self.M2

    def set_M2(self, M2):
        self.M2 = M2
        self.e_phase.M = self.M2
        self.e_mpam_ph.M = self.M2
        self.e_c_p.M = self.M2
        self.b_u_de_M_PAM_bb_0.set_M(self.M2)
        self.b_u_M_PAM_bb_0.set_M(self.M2)
        self.set_BpS2(int(math.log(self.M2,2)))

    def get_Rb2(self):
        return self.Rb2

    def set_Rb2(self, Rb2):
        self.Rb2 = Rb2
        self.set_Rs2(self.Rb2/self.BpS2)

    def get_BpS2(self):
        return self.BpS2

    def set_BpS2(self, BpS2):
        self.BpS2 = BpS2
        self.set_Rs2(self.Rb2/self.BpS2)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_Rs2(self):
        return self.Rs2

    def set_Rs2(self, Rs2):
        self.Rs2 = Rs2
        self.b_BERTool_0_0_0.set_Rs(self.Rs2)

    def get_N_snr(self):
        return self.N_snr

    def set_N_snr(self, N_snr):
        self.N_snr = N_snr
        self.qtgui_vector_sink_f_0.set_x_axis(self.EsN0min, (self.EsN0max-self.EsN0min)/float(self.N_snr))
        self.b_BERTool_0_0_0.set_N_snr(self.N_snr)

    def get_EsN0min(self):
        return self.EsN0min

    def set_EsN0min(self, EsN0min):
        self.EsN0min = EsN0min
        self.qtgui_vector_sink_f_0.set_x_axis(self.EsN0min, (self.EsN0max-self.EsN0min)/float(self.N_snr))
        self.b_BERTool_0_0_0.set_EsN0min(self.EsN0min)

    def get_EsN0max(self):
        return self.EsN0max

    def set_EsN0max(self, EsN0max):
        self.EsN0max = EsN0max
        self.qtgui_vector_sink_f_0.set_x_axis(self.EsN0min, (self.EsN0max-self.EsN0min)/float(self.N_snr))
        self.b_BERTool_0_0_0.set_EsN0max(self.EsN0max)


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
