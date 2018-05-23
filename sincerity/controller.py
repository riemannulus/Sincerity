import time

import audioop
import pyaudio

from numpy import mean, std
from numpy.fft import fft

from module import *


class DataGetter():

    def __init__(self, audio_data):
        self.audio_data=audio_data
        self.channels=audio_data.channels
        self.rate=audio_data.rate
        self.chunk=audio_data.chunk

    def get_signal_buffer(self, end_gap):
        input = PyAudioInput(self.audio_data)
        start_time = time.time()
        buffer = []
        while(True):
            samples = input.read()
            if not len(samples):
                continue

            spectrum = get_spectrum(samples)
            freq = get_peak_frequency(spectrum, self.rate)

            now = time.time()
            buffer.append(freq)
            if now - start_time > end_gap:
                input.stop()
                return buffer

def get_highest_prequency(buf1, buf2, buf3):

    def compare(s1, s2):
        if s1[0] > s2[0]:
            return s1
        else:
            return s2

    signal_temp = list(map(compare, buf1, buf2))

    return list(map(compare, signal_temp, buf3))


def get_lowest_prequency(buf1, buf2, buf3):

    def compare(s1, s2):
        if s1[0] > s2[0]:
            return s2
        else:
            return s1

    signal_temp = list(map(compare, buf1, buf2))

    return list(map(compare, signal_temp, buf3))

# Compare volume power by pivot
# if is lower then pivot, remove it
# if is higher then pivot, stop loop
# and reprocessing from backword
def process_signal(buf, pivot):

    try:
        process_buf = buf[:]
        for signal in buf:
            if signal[1] < pivot:
                process_buf.remove(signal)
            else:
                break

        for signal in buf[::-1]:
            if signal[1] < pivot:
                process_buf.remove(signal)
            else:
                break

    except ValueError:
        pass

    return process_buf
