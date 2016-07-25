#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Power
# Generated: Mon Jul 25 09:22:30 2016
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

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class Power(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Power")

        ##################################################
        # Variables
        ##################################################
        self.vect_len = vect_len = 1024
        self.samp_rate = samp_rate = 20
        self.mean_length = mean_length = 1
        self.freq = freq = 5.8e09
        self.MuteTx = MuteTx = False

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_1 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_1.win)
        self.wxgui_numbersink2_1 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit="mW",
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=2,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=1,
        	average=True,
        	avg_alpha=1,
        	label="Average received power (mW)",
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_1.win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec("A:B", 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0.set_gain(56, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_subdev_spec("A:A", 0)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(freq, 0)
        self.uhd_usrp_sink_0.set_gain(56, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, mean_length, 1, firdes.WIN_HAMMING, 6.76))
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, vect_len)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, vect_len)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vff((1000, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((1000, ))
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*vect_len, "/home/moez/Desktop/data_7_15/wTx_A_1", False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*vect_len, "/home/moez/Desktop/data_7_15/wRx_A_1", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_1 = blocks.complex_to_mag(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, mean_length, 1, 0)
        self._MuteTx_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.MuteTx,
        	callback=self.set_MuteTx,
        	label='MuteTx',
        	true=True,
        	false=False,
        )
        self.Add(self._MuteTx_check_box)
        self.Mute = blocks.mute_cc(bool(MuteTx))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Mute, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.Mute, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.Mute, 0))    
        self.connect((self.blocks_complex_to_mag_1, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_complex_to_mag_1, 0), (self.wxgui_scopesink2_1, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_multiply_const_vxx_2, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.wxgui_numbersink2_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.blocks_file_sink_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_1, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))    

    def get_vect_len(self):
        return self.vect_len

    def set_vect_len(self, vect_len):
        self.vect_len = vect_len

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.mean_length, 1, firdes.WIN_HAMMING, 6.76))
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate)

    def get_mean_length(self):
        return self.mean_length

    def set_mean_length(self, mean_length):
        self.mean_length = mean_length
        self.analog_sig_source_x_0.set_frequency(self.mean_length)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.mean_length, 1, firdes.WIN_HAMMING, 6.76))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_sink_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.freq, 1)

    def get_MuteTx(self):
        return self.MuteTx

    def set_MuteTx(self, MuteTx):
        self.MuteTx = MuteTx
        self._MuteTx_check_box.set_value(self.MuteTx)
        self.Mute.set_mute(bool(self.MuteTx))


def main(top_block_cls=Power, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
