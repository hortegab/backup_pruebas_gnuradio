#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: SER Simulation
# Author: Homero Ortega Boada
# Description: Dale un valor a Es/No, corre el flujograma y obten la SER. Puedes sacar tantos valores como para construir una curva de SER
# Generated: Mon Mar  2 17:30:07 2020
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

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import cmath
import coding  # embedded python module
import math
import numpy as np
import sip
import sys
from gnuradio import qtgui


class ser_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "SER Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("SER Simulation")
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

        self.settings = Qt.QSettings("GNU Radio", "ser_simulation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################

        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((digital.constellation_8psk().points()), (), 0, 1).base()

        self.samp_rate = samp_rate = 100e3
        self.Sps = Sps = 1
        self.M = M = len(MiconstellationObject.points())
        self.Rs = Rs = samp_rate/Sps
        self.Bps = Bps = int(math.log(M,2))
        self.simb = simb = 2
        self.run_stop = run_stop = True
        self.phi_desv = phi_desv = 0
        self.phi_const = phi_const = 2*math.pi/4
        self.mapinverse = mapinverse = coding.inverse_map(MiconstellationObject.points())
        self.mapdirect = mapdirect = coding.direct_map(MiconstellationObject.points())
        self.Rb = Rb = Rs*Bps
        self.Npuntosgira = Npuntosgira = 1

        ##################################################
        # Blocks
        ##################################################
        self._simb_tool_bar = Qt.QToolBar(self)
        self._simb_tool_bar.addWidget(Qt.QLabel('simb'+": "))
        self._simb_line_edit = Qt.QLineEdit(str(self.simb))
        self._simb_tool_bar.addWidget(self._simb_line_edit)
        self._simb_line_edit.returnPressed.connect(
        	lambda: self.set_simb(int(str(self._simb_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._simb_tool_bar, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 20)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 2, 0, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-1, 1)
        self.qtgui_const_sink_x_0.set_x_axis(-1, 1)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_map_bb_0_0 = digital.map_bb((mapinverse))
        self.digital_map_bb_0 = digital.map_bb((mapdirect))
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(M)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(M)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(MiconstellationObject)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((MiconstellationObject.points()), 1)
        self.blocks_vector_source_x_0 = blocks.vector_source_b((0,1,2,3,4,5,6,7), True, 1, [])
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((cmath.exp(phi_desv*1.j), ))
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.digital_diff_decoder_bb_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ser_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.set_Rs(self.samp_rate/self.Sps)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_Rs(self.samp_rate/self.Sps)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Rb(self.Rs*self.Bps)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Rb(self.Rs*self.Bps)

    def get_simb(self):
        return self.simb

    def set_simb(self, simb):
        self.simb = simb
        Qt.QMetaObject.invokeMethod(self._simb_line_edit, "setText", Qt.Q_ARG("QString", str(self.simb)))

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_phi_desv(self):
        return self.phi_desv

    def set_phi_desv(self, phi_desv):
        self.phi_desv = phi_desv
        self.blocks_multiply_const_vxx_0.set_k((cmath.exp(self.phi_desv*1.j), ))

    def get_phi_const(self):
        return self.phi_const

    def set_phi_const(self, phi_const):
        self.phi_const = phi_const

    def get_mapinverse(self):
        return self.mapinverse

    def set_mapinverse(self, mapinverse):
        self.mapinverse = mapinverse

    def get_mapdirect(self):
        return self.mapdirect

    def set_mapdirect(self, mapdirect):
        self.mapdirect = mapdirect

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb

    def get_Npuntosgira(self):
        return self.Npuntosgira

    def set_Npuntosgira(self, Npuntosgira):
        self.Npuntosgira = Npuntosgira


def main(top_block_cls=ser_simulation, options=None):

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
