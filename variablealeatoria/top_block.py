#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu May  9 09:31:51 2019
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
from b_v_aleatoria_scope_f import b_v_aleatoria_scope_f  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import E3TRadio
import formas  # embedded python module
import numpy
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
        self.samp_rate = samp_rate = 1953125
        self.Sps = Sps = 8
        self.samp_rate_audio = samp_rate_audio = 11000
        self.run_stop = run_stop = True
        self.rolloff = rolloff = 1
        self.ntaps = ntaps = 128
        self.Rs = Rs = samp_rate/Sps

        ##################################################
        # Blocks
        ##################################################
        self.Menu = Qt.QTabWidget()
        self.Menu_widget_0 = Qt.QWidget()
        self.Menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_0)
        self.Menu_grid_layout_0 = Qt.QGridLayout()
        self.Menu_layout_0.addLayout(self.Menu_grid_layout_0)
        self.Menu.addTab(self.Menu_widget_0, 'banary random signal')
        self.Menu_widget_1 = Qt.QWidget()
        self.Menu_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_1)
        self.Menu_grid_layout_1 = Qt.QGridLayout()
        self.Menu_layout_1.addLayout(self.Menu_grid_layout_1)
        self.Menu.addTab(self.Menu_widget_1, 'sinc wave form random signal')
        self.Menu_widget_2 = Qt.QWidget()
        self.Menu_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_2)
        self.Menu_grid_layout_2 = Qt.QGridLayout()
        self.Menu_layout_2.addLayout(self.Menu_grid_layout_2)
        self.Menu.addTab(self.Menu_widget_2, 'saw random signal')
        self.Menu_widget_3 = Qt.QWidget()
        self.Menu_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_3)
        self.Menu_grid_layout_3 = Qt.QGridLayout()
        self.Menu_layout_3.addLayout(self.Menu_grid_layout_3)
        self.Menu.addTab(self.Menu_widget_3, 'gaussian white noise')
        self.Menu_widget_4 = Qt.QWidget()
        self.Menu_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.Menu_widget_4)
        self.Menu_grid_layout_4 = Qt.QGridLayout()
        self.Menu_layout_4.addLayout(self.Menu_grid_layout_4)
        self.Menu.addTab(self.Menu_widget_4, 'voice noise')
        self.top_grid_layout.addWidget(self.Menu, 1, 0, 1, 4)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
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
        self.interp_fir_filter_xxx_0_1 = filter.interp_fir_filter_fff(Sps, (formas.saw(Sps)/Sps))
        self.interp_fir_filter_xxx_0_1.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(Sps, (formas.ventana(Sps)))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(Sps, (formas.sinc(Sps,ntaps)))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/media/uis-e3t/DATADRIVE1/MisGitHub/comdig2.Lab2.4/bush-clinton_debate_waffle.wav', True)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.b_v_aleatoria_scope_f_0_0_2 = b_v_aleatoria_scope_f(
            N_frec=1024,
            N_time=20*Sps,
            V_p=1.5,
            samp_rate=samp_rate,
        )
        self.Menu_grid_layout_4.addWidget(self.b_v_aleatoria_scope_f_0_0_2, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_4.setColumnStretch(c, 1)
        self.b_v_aleatoria_scope_f_0_0_1 = b_v_aleatoria_scope_f(
            N_frec=1024,
            N_time=20*Sps,
            V_p=3.,
            samp_rate=samp_rate,
        )
        self.Menu_grid_layout_3.addWidget(self.b_v_aleatoria_scope_f_0_0_1, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_3.setColumnStretch(c, 1)
        self.b_v_aleatoria_scope_f_0_0_0 = b_v_aleatoria_scope_f(
            N_frec=1024,
            N_time=20*Sps,
            V_p=1.5,
            samp_rate=samp_rate,
        )
        self.Menu_grid_layout_2.addWidget(self.b_v_aleatoria_scope_f_0_0_0, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_2.setColumnStretch(c, 1)
        self.b_v_aleatoria_scope_f_0_0 = b_v_aleatoria_scope_f(
            N_frec=1024,
            N_time=20*Sps,
            V_p=1.5,
            samp_rate=samp_rate,
        )
        self.Menu_grid_layout_1.addWidget(self.b_v_aleatoria_scope_f_0_0, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_1.setColumnStretch(c, 1)
        self.b_v_aleatoria_scope_f_0 = b_v_aleatoria_scope_f(
            N_frec=1024,
            N_time=20*Sps,
            V_p=1.5,
            samp_rate=samp_rate,
        )
        self.Menu_grid_layout_0.addWidget(self.b_v_aleatoria_scope_f_0, 0, 0, 1, 1)
        for r in range(0, 1):
            self.Menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.Menu_grid_layout_0.setColumnStretch(c, 1)
        self.analog_random_source_x_0 = blocks.vector_source_i(map(int, numpy.random.randint(0, 2, 1000000)), True)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 1, 0)
        self.E3TRadio_unipolar_to_bipolar_ff_0 = E3TRadio.unipolar_to_bipolar_ff(1.)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.E3TRadio_unipolar_to_bipolar_ff_0, 0), (self.interp_fir_filter_xxx_0_1, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.b_v_aleatoria_scope_f_0_0_1, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.E3TRadio_unipolar_to_bipolar_ff_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.b_v_aleatoria_scope_f_0_0_2, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.b_v_aleatoria_scope_f_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.b_v_aleatoria_scope_f_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_1, 0), (self.b_v_aleatoria_scope_f_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_v_aleatoria_scope_f_0_0_2.set_samp_rate(self.samp_rate)
        self.b_v_aleatoria_scope_f_0_0_1.set_samp_rate(self.samp_rate)
        self.b_v_aleatoria_scope_f_0_0_0.set_samp_rate(self.samp_rate)
        self.b_v_aleatoria_scope_f_0_0.set_samp_rate(self.samp_rate)
        self.b_v_aleatoria_scope_f_0.set_samp_rate(self.samp_rate)
        self.set_Rs(self.samp_rate/self.Sps)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.interp_fir_filter_xxx_0_1.set_taps((formas.saw(self.Sps)/self.Sps))
        self.interp_fir_filter_xxx_0_0.set_taps((formas.ventana(self.Sps)))
        self.interp_fir_filter_xxx_0.set_taps((formas.sinc(self.Sps,self.ntaps)))
        self.b_v_aleatoria_scope_f_0_0_2.set_N_time(20*self.Sps)
        self.b_v_aleatoria_scope_f_0_0_1.set_N_time(20*self.Sps)
        self.b_v_aleatoria_scope_f_0_0_0.set_N_time(20*self.Sps)
        self.b_v_aleatoria_scope_f_0_0.set_N_time(20*self.Sps)
        self.b_v_aleatoria_scope_f_0.set_N_time(20*self.Sps)
        self.set_Rs(self.samp_rate/self.Sps)

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.interp_fir_filter_xxx_0.set_taps((formas.sinc(self.Sps,self.ntaps)))

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs


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
