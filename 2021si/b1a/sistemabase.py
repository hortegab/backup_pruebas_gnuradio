#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: sistemabase
# Author: homero
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from b_EYE_Timing_f import b_EYE_Timing_f  # grc-generated hier_block
from b_PSD_f import b_PSD_f  # grc-generated hier_block
from b_bipolar_to_unipolar_ff import b_bipolar_to_unipolar_ff  # grc-generated hier_block
from b_unipolar2bipolar_ff import b_unipolar2bipolar_ff  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import E3TRadio
import mis_funciones  # embedded python module



from gnuradio import qtgui

class sistemabase(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "sistemabase", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("sistemabase")
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

        self.settings = Qt.QSettings("GNU Radio", "sistemabase")

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
        self.Sps = Sps = 8
        self.Rb = Rb = 32000
        self.Nlob_n = Nlob_n = 6
        self.samp_rate = samp_rate = Rb*Sps
        self.ntaps = ntaps = Nlob_n*Sps
        self.alpha = alpha = 0.5
        self.samp_rate_dac = samp_rate_dac = samp_rate*32
        self.h2 = h2 = mis_funciones.rrcos(Sps,ntaps,alpha)
        self.h1 = h1 = mis_funciones.rcos(Sps,ntaps,alpha)
        self.h0 = h0 = ([1]*Sps)
        self.Retardo_bits = Retardo_bits = 0
        self.Noise = Noise = 0.2
        self.Dtiming = Dtiming = 7
        self.BW = BW = samp_rate/2

        ##################################################
        # Blocks
        ##################################################
        self._Retardo_bits_range = Range(0, Sps*10, 1, 0, 200)
        self._Retardo_bits_win = RangeWidget(self._Retardo_bits_range, self.set_Retardo_bits, 'Delay transmited signal to match with the received signal', "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Retardo_bits_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Noise_range = Range(0, 4, 0.1, 0.2, 200)
        self._Noise_win = RangeWidget(self._Noise_range, self.set_Noise, 'Noise', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Noise_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.Menu = Qt.QTabWidget()
        self.Menu_widget_0 = Qt.QWidget()
        self.Menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_0)
        self.Menu_grid_layout_0 = Qt.QGridLayout()
        self.Menu_layout_0.addLayout(self.Menu_grid_layout_0)
        self.Menu.addTab(self.Menu_widget_0, 'T1 R1')
        self.Menu_widget_1 = Qt.QWidget()
        self.Menu_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_1)
        self.Menu_grid_layout_1 = Qt.QGridLayout()
        self.Menu_layout_1.addLayout(self.Menu_grid_layout_1)
        self.Menu.addTab(self.Menu_widget_1, 'T2 R2')
        self.Menu_widget_2 = Qt.QWidget()
        self.Menu_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_2)
        self.Menu_grid_layout_2 = Qt.QGridLayout()
        self.Menu_layout_2.addLayout(self.Menu_grid_layout_2)
        self.Menu.addTab(self.Menu_widget_2, 'T3 R3')
        self.Menu_widget_3 = Qt.QWidget()
        self.Menu_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_3)
        self.Menu_grid_layout_3 = Qt.QGridLayout()
        self.Menu_layout_3.addLayout(self.Menu_grid_layout_3)
        self.Menu.addTab(self.Menu_widget_3, 'Eye Diagramm')
        self.Menu_widget_4 = Qt.QWidget()
        self.Menu_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_4)
        self.Menu_grid_layout_4 = Qt.QGridLayout()
        self.Menu_layout_4.addLayout(self.Menu_grid_layout_4)
        self.Menu.addTab(self.Menu_widget_4, 'Timing')
        self.top_grid_layout.addWidget(self.Menu, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Dtiming_range = Range(0, Sps-1, 1, 7, 200)
        self._Dtiming_win = RangeWidget(self._Dtiming_range, self.set_Dtiming, 'Dtiming', "counter_slider", int, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Dtiming_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            ntaps, #size
            samp_rate, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['T2', 'R2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [2, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.Menu_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            ntaps, #size
            Rb, #samp_rate
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(True)


        labels = ['T1', 'R1', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [2, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [0, 7, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(3):
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
        self.Menu_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_eye_sink_x_0 = qtgui.eye_sink_f(
            1024, #size
            samp_rate, #samp_rate
            2, #number of inputs
            None
        )
        self.qtgui_eye_sink_x_0.set_update_time(0.10)
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(Sps)
        self.qtgui_eye_sink_x_0.set_y_axis(-6, 6)

        self.qtgui_eye_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_eye_sink_x_0.enable_tags(True)
        self.qtgui_eye_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_eye_sink_x_0.enable_autoscale(False)
        self.qtgui_eye_sink_x_0.enable_grid(False)
        self.qtgui_eye_sink_x_0.enable_axis_labels(True)
        self.qtgui_eye_sink_x_0.enable_control_panel(False)


        labels = ['R2', 'R2.0', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [4, 4, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'blue', 'blue', 'blue', 'blue',
            'blue', 'blue', 'blue', 'blue', 'blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_eye_sink_x_0.set_line_label(i, "Eye[Data {0}]".format(i))
            else:
                self.qtgui_eye_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_eye_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_eye_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_eye_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_eye_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_eye_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_eye_sink_x_0_win = sip.wrapinstance(self.qtgui_eye_sink_x_0.pyqwidget(), Qt.QWidget)
        self.Menu_grid_layout_3.addWidget(self._qtgui_eye_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_3.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(1, h0)
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(Sps, h0)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(1/Sps)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/radiogis_director/MisGits/comdiguispractices2021si.3.8/unit I/Pract1.basic system based in rectangular pulse form/enviado.jpg', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/radiogis_director/MisGits/comdiguis_b1a_2021si/Fase I/received', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, Retardo_bits)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.b_unipolar2bipolar_ff_0 = b_unipolar2bipolar_ff()
        self.b_bipolar_to_unipolar_ff_0 = b_bipolar_to_unipolar_ff()
        self.b_PSD_f_0 = b_PSD_f(
            Ensayos=1000000,
            N=1024,
            Titulo='espectro',
            Ymax=4e-6,
            samp_rate=samp_rate,
        )

        self.Menu_grid_layout_1.addWidget(self.b_PSD_f_0, 1, 0, 1, 1)
        for r in range(1, 2):
            self.Menu_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_1.setColumnStretch(c, 1)
        self.b_EYE_Timing_f_0 = b_EYE_Timing_f(
            AlphaLineas=0.5,
            Delay=0,
            GrosorLineas=20,
            N_eyes=2,
            Retardo_Timing=Dtiming,
            Samprate=samp_rate,
            Sps=Sps,
            Title="Eye Diagram and Timing",
            Ymax=2,
            Ymin=-2,
        )

        self.Menu_grid_layout_4.addWidget(self.b_EYE_Timing_f_0, 1, 0, 1, 1)
        for r in range(1, 2):
            self.Menu_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_4.setColumnStretch(c, 1)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, Noise, 0)
        self.E3TRadio_diezma_ff_0 = E3TRadio.diezma_ff(Sps, Dtiming)
        self.E3TRadio_bipolar_decisor_ff_0 = E3TRadio.bipolar_decisor_ff()



        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_bipolar_decisor_ff_0, 0), (self.b_bipolar_to_unipolar_ff_0, 0))
        self.connect((self.E3TRadio_bipolar_decisor_ff_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.E3TRadio_diezma_ff_0, 0), (self.E3TRadio_bipolar_decisor_ff_0, 0))
        self.connect((self.E3TRadio_diezma_ff_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.b_bipolar_to_unipolar_ff_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.b_unipolar2bipolar_ff_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.b_unipolar2bipolar_ff_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_eye_sink_x_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.blocks_char_to_float_1, 0), (self.b_unipolar2bipolar_ff_0, 0))
        self.connect((self.blocks_delay_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.E3TRadio_diezma_ff_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.b_EYE_Timing_f_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_eye_sink_x_0, 1))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.b_PSD_f_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "sistemabase")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_h0(([1]*self.Sps))
        self.set_h1(mis_funciones.rcos(self.Sps,self.ntaps,self.alpha))
        self.set_h2(mis_funciones.rrcos(self.Sps,self.ntaps,self.alpha))
        self.set_ntaps(self.Nlob_n*self.Sps)
        self.set_samp_rate(self.Rb*self.Sps)
        self.b_EYE_Timing_f_0.set_Sps(self.Sps)
        self.blocks_multiply_const_vxx_0.set_k(1/self.Sps)
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(self.Sps)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_samp_rate(self.Rb*self.Sps)
        self.qtgui_time_sink_x_0.set_samp_rate(self.Rb)

    def get_Nlob_n(self):
        return self.Nlob_n

    def set_Nlob_n(self, Nlob_n):
        self.Nlob_n = Nlob_n
        self.set_ntaps(self.Nlob_n*self.Sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_BW(self.samp_rate/2)
        self.set_samp_rate_dac(self.samp_rate*32)
        self.b_EYE_Timing_f_0.set_Samprate(self.samp_rate)
        self.b_PSD_f_0.set_samp_rate(self.samp_rate)
        self.qtgui_eye_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_h1(mis_funciones.rcos(self.Sps,self.ntaps,self.alpha))
        self.set_h2(mis_funciones.rrcos(self.Sps,self.ntaps,self.alpha))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.set_h1(mis_funciones.rcos(self.Sps,self.ntaps,self.alpha))
        self.set_h2(mis_funciones.rrcos(self.Sps,self.ntaps,self.alpha))

    def get_samp_rate_dac(self):
        return self.samp_rate_dac

    def set_samp_rate_dac(self, samp_rate_dac):
        self.samp_rate_dac = samp_rate_dac

    def get_h2(self):
        return self.h2

    def set_h2(self, h2):
        self.h2 = h2

    def get_h1(self):
        return self.h1

    def set_h1(self, h1):
        self.h1 = h1

    def get_h0(self):
        return self.h0

    def set_h0(self, h0):
        self.h0 = h0
        self.interp_fir_filter_xxx_0.set_taps(self.h0)
        self.interp_fir_filter_xxx_0_0.set_taps(self.h0)

    def get_Retardo_bits(self):
        return self.Retardo_bits

    def set_Retardo_bits(self, Retardo_bits):
        self.Retardo_bits = Retardo_bits
        self.blocks_delay_1.set_dly(self.Retardo_bits)

    def get_Noise(self):
        return self.Noise

    def set_Noise(self, Noise):
        self.Noise = Noise
        self.analog_noise_source_x_0.set_amplitude(self.Noise)

    def get_Dtiming(self):
        return self.Dtiming

    def set_Dtiming(self, Dtiming):
        self.Dtiming = Dtiming
        self.E3TRadio_diezma_ff_0.set_ka(self.Dtiming)
        self.b_EYE_Timing_f_0.set_Retardo_Timing(self.Dtiming)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW




def main(top_block_cls=sistemabase, options=None):

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
