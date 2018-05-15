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
            print(freq)

            now = time.time()
            buffer.append(freq)
            if now - start_time > end_gap:
                input.stop()
                return buffer


