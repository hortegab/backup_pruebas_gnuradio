#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BER Simulation
# Author: Example
# Description: Adjust the noise and constellation... see what happens!
# Generated: Thu Mar 19 20:38:27 2020
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
from b_PSD_c import b_PSD_c  # grc-generated hier_block
from b_quantizer_fb import b_quantizer_fb  # grc-generated hier_block
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import E3TRadio
import coding  # embedded python module
import math
import numpy
import random
import sip
import wform  # embedded python module
from gnuradio import qtgui


class ber_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "BER Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BER Simulation")
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

        self.settings = Qt.QSettings("GNU Radio", "ber_simulation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################

        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((digital.constellation_bpsk().points()), (), 4, 1).base()

        self.Constelacion = Constelacion = MiconstellationObject.points()
        self.samp_rate_audio = samp_rate_audio = 44100
        self.NbpS = NbpS = 8
        self.M = M = len(Constelacion)
        self.samp_rate_usrp_rx = samp_rate_usrp_rx = 100e6
        self.Rb = Rb = NbpS*samp_rate_audio
        self.Bps = Bps = int(math.log(M,2))
        self.samp_rate_to_usrp = samp_rate_to_usrp = int(samp_rate_usrp_rx/128)
        self.Rs = Rs = Rb/Bps
        self.ntaps = ntaps = 128
        self.Sps = Sps = int(math.floor(samp_rate_to_usrp/Rs))
        self.Rolloff = Rolloff = 0.5
        self.samp_rate = samp_rate = Rs*Sps
        self.run_stop = run_stop = True
        self.mapinverse = mapinverse = coding.inverse_map(Constelacion)
        self.mapdirect = mapdirect = coding.direct_map(Constelacion)
        self.h_rrc = h_rrc = wform.rrcos(Sps,ntaps,Rolloff)
        self.Vp = Vp = 1.
        self.TimeAligment = TimeAligment = 7
        self.Sps_t = Sps_t = Sps*16
        self.Retardo_propag = Retardo_propag = int(ntaps/Sps)+1
        self.Retardo_Timing = Retardo_Timing = 11
        self.Ph_correction = Ph_correction = 0
        self.NnivelesQ = NnivelesQ = math.pow(2,NbpS)
        self.BW = BW = (Rs/2)*(1+Rolloff)

        ##################################################
        # Blocks
        ##################################################
        self.menu = Qt.QTabWidget()
        self.menu_widget_0 = Qt.QWidget()
        self.menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_0)
        self.menu_grid_layout_0 = Qt.QGridLayout()
        self.menu_layout_0.addLayout(self.menu_grid_layout_0)
        self.menu.addTab(self.menu_widget_0, 'Constelation Timing')
        self.menu_widget_1 = Qt.QWidget()
        self.menu_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_1)
        self.menu_grid_layout_1 = Qt.QGridLayout()
        self.menu_layout_1.addLayout(self.menu_grid_layout_1)
        self.menu.addTab(self.menu_widget_1, 'Senal MPAM')
        self.menu_widget_2 = Qt.QWidget()
        self.menu_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_2)
        self.menu_grid_layout_2 = Qt.QGridLayout()
        self.menu_layout_2.addLayout(self.menu_grid_layout_2)
        self.menu.addTab(self.menu_widget_2, 'PSD en R1a')
        self.menu_widget_3 = Qt.QWidget()
        self.menu_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_3)
        self.menu_grid_layout_3 = Qt.QGridLayout()
        self.menu_layout_3.addLayout(self.menu_grid_layout_3)
        self.menu.addTab(self.menu_widget_3, 'senal en el cable')
        self.top_grid_layout.addWidget(self.menu, 2, 0, 1, 4)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._TimeAligment_range = Range(0, Sps*20, 1, 7, 200)
        self._TimeAligment_win = RangeWidget(self._TimeAligment_range, self.set_TimeAligment, 'TimeAligment', "counter_slider", int)
        self.top_grid_layout.addWidget(self._TimeAligment_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Retardo_Timing_range = Range(0, Sps*16-1, 1, 11, 200)
        self._Retardo_Timing_win = RangeWidget(self._Retardo_Timing_range, self.set_Retardo_Timing, 'Timing', "counter_slider", int)
        self.top_grid_layout.addWidget(self._Retardo_Timing_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Ph_correction_range = Range(-numpy.pi, numpy.pi, 2*numpy.pi/720., 0, 200)
        self._Ph_correction_win = RangeWidget(self._Ph_correction_range, self.set_Ph_correction, 'PLL Correction', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Ph_correction_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox('Pause')
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
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_ccc(
                interpolation=Rs*Sps_t,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate,
                decimation=samp_rate_to_usrp,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate_to_usrp,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['T4', 'R4', '', '', '',
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
        for i in xrange(2):
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
        self.menu_grid_layout_0.addWidget(self._qtgui_const_sink_x_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.menu_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_0.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0_0_0_0 = filter.interp_fir_filter_ccc(1, (h_rrc))
        self.interp_fir_filter_xxx_0_0_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_0 = filter.interp_fir_filter_ccc(Sps, (h_rrc))
        self.interp_fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self.digital_map_bb_0_0 = digital.map_bb((mapinverse))
        self.digital_map_bb_0 = digital.map_bb((mapdirect))
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(M)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(M)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(MiconstellationObject)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((MiconstellationObject.points()), 1)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/uis-e3t/MisGits/comdig_pract_DiffCod_PLL/pruebas/DudaEstudiante/set-fire-to-the-rain.wav', True)
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(Bps, gr.GR_LSB_FIRST)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate_to_usrp,True)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(Bps, gr.GR_LSB_FIRST)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((0.7, ))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((Vp/(NnivelesQ/2)/2, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1./Sps, ))
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_char*1, TimeAligment)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, Sps_t-Retardo_Timing)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.b_quantizer_fb_0 = b_quantizer_fb(
            NivelesQ=NnivelesQ,
            Vmax=Vp,
        )
        self.b_PSD_c_0 = b_PSD_c(
            Ensayos=1000000,
            Fc=0,
            N=1024,
            Titulo='PSD in R1a',
            Ymax=1e-5,
            samp_rate_audio=samp_rate,
        )
        self.menu_grid_layout_2.addWidget(self.b_PSD_c_0, 2, 0, 1, 1)
        for r in range(2, 3):
            self.menu_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.menu_grid_layout_2.setColumnStretch(c, 1)
        self.audio_sink_0 = audio.sink(samp_rate_audio, '', True)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, numpy.exp(Ph_correction*1.j))
        self._Retardo_propag_range = Range(0, Sps*200, 1, int(ntaps/Sps)+1, 200)
        self._Retardo_propag_win = RangeWidget(self._Retardo_propag_range, self.set_Retardo_propag, 'Propagation delay compensation', "counter_slider", int)
        self.top_grid_layout.addWidget(self._Retardo_propag_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.E3TRadio_diezmador_cc_0 = E3TRadio.diezmador_cc(Sps_t)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_diezmador_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.E3TRadio_diezmador_cc_0, 0), (self.qtgui_const_sink_x_0, 1))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.b_quantizer_fb_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.E3TRadio_diezmador_cc_0, 0))
        self.connect((self.blocks_delay_0_0_0, 0), (self.blocks_unpacked_to_packed_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.interp_fir_filter_xxx_0_0_0_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.b_quantizer_fb_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.interp_fir_filter_xxx_0_0_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_delay_0_0_0, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.b_PSD_c_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.blocks_delay_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ber_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_mapinverse(coding.inverse_map(self.Constelacion))
        self.set_mapdirect(coding.direct_map(self.Constelacion))
        self.set_M(len(self.Constelacion))

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio
        self.set_Rb(self.NbpS*self.samp_rate_audio)

    def get_NbpS(self):
        return self.NbpS

    def set_NbpS(self, NbpS):
        self.NbpS = NbpS
        self.set_NnivelesQ(math.pow(2,self.NbpS))
        self.set_Rb(self.NbpS*self.samp_rate_audio)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))

    def get_samp_rate_usrp_rx(self):
        return self.samp_rate_usrp_rx

    def set_samp_rate_usrp_rx(self, samp_rate_usrp_rx):
        self.samp_rate_usrp_rx = samp_rate_usrp_rx
        self.set_samp_rate_to_usrp(int(self.samp_rate_usrp_rx/128))

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_Rs(self.Rb/self.Bps)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Rs(self.Rb/self.Bps)

    def get_samp_rate_to_usrp(self):
        return self.samp_rate_to_usrp

    def set_samp_rate_to_usrp(self, samp_rate_to_usrp):
        self.samp_rate_to_usrp = samp_rate_to_usrp
        self.set_Sps(int(math.floor(self.samp_rate_to_usrp/self.Rs)))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate_to_usrp)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Sps(int(math.floor(self.samp_rate_to_usrp/self.Rs)))
        self.set_samp_rate(self.Rs*self.Sps)
        self.set_BW((self.Rs/2)*(1+self.Rolloff))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_h_rrc(wform.rrcos(self.Sps,self.ntaps,self.Rolloff))
        self.set_Retardo_propag(int(self.ntaps/self.Sps)+1)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_samp_rate(self.Rs*self.Sps)
        self.set_h_rrc(wform.rrcos(self.Sps,self.ntaps,self.Rolloff))
        self.set_Sps_t(self.Sps*16)
        self.blocks_multiply_const_vxx_0.set_k((1./self.Sps, ))
        self.set_Retardo_propag(int(self.ntaps/self.Sps)+1)

    def get_Rolloff(self):
        return self.Rolloff

    def set_Rolloff(self, Rolloff):
        self.Rolloff = Rolloff
        self.set_h_rrc(wform.rrcos(self.Sps,self.ntaps,self.Rolloff))
        self.set_BW((self.Rs/2)*(1+self.Rolloff))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.b_PSD_c_0.set_samp_rate_audio(self.samp_rate)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        self._run_stop_callback(self.run_stop)
        if self.run_stop: self.start()
        else: self.stop(); self.wait()

    def get_mapinverse(self):
        return self.mapinverse

    def set_mapinverse(self, mapinverse):
        self.mapinverse = mapinverse

    def get_mapdirect(self):
        return self.mapdirect

    def set_mapdirect(self, mapdirect):
        self.mapdirect = mapdirect

    def get_h_rrc(self):
        return self.h_rrc

    def set_h_rrc(self, h_rrc):
        self.h_rrc = h_rrc
        self.interp_fir_filter_xxx_0_0_0_0.set_taps((self.h_rrc))
        self.interp_fir_filter_xxx_0_0_0.set_taps((self.h_rrc))

    def get_Vp(self):
        return self.Vp

    def set_Vp(self, Vp):
        self.Vp = Vp
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.Vp/(self.NnivelesQ/2)/2, ))
        self.b_quantizer_fb_0.set_Vmax(self.Vp)

    def get_TimeAligment(self):
        return self.TimeAligment

    def set_TimeAligment(self, TimeAligment):
        self.TimeAligment = TimeAligment
        self.blocks_delay_0_0_0.set_dly(self.TimeAligment)

    def get_Sps_t(self):
        return self.Sps_t

    def set_Sps_t(self, Sps_t):
        self.Sps_t = Sps_t
        self.blocks_delay_0_0.set_dly(self.Sps_t-self.Retardo_Timing)

    def get_Retardo_propag(self):
        return self.Retardo_propag

    def set_Retardo_propag(self, Retardo_propag):
        self.Retardo_propag = Retardo_propag

    def get_Retardo_Timing(self):
        return self.Retardo_Timing

    def set_Retardo_Timing(self, Retardo_Timing):
        self.Retardo_Timing = Retardo_Timing
        self.blocks_delay_0_0.set_dly(self.Sps_t-self.Retardo_Timing)

    def get_Ph_correction(self):
        return self.Ph_correction

    def set_Ph_correction(self, Ph_correction):
        self.Ph_correction = Ph_correction
        self.analog_const_source_x_0.set_offset(numpy.exp(self.Ph_correction*1.j))

    def get_NnivelesQ(self):
        return self.NnivelesQ

    def set_NnivelesQ(self, NnivelesQ):
        self.NnivelesQ = NnivelesQ
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.Vp/(self.NnivelesQ/2)/2, ))
        self.b_quantizer_fb_0.set_NivelesQ(self.NnivelesQ)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW


def main(top_block_cls=ber_simulation, options=None):

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
