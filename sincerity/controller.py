import time

import audioop
import pyaudio

from numpy import mean, std
from numpy.fft import fft

from module import PyAudioInput, PyAudioData

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

        def get_spectrum(samples):
            result = fft(samples)
            return result[:int(len(result)/2)]

        def get_peak_frequency(spectrum, rate):
            best = -1
            best_idx = 0
            for n in range(len(spectrum)):
                if abs(spectrum[n]) > best:
                    best = abs(spectrum[n])
                    best_idx = n

            peak_frequency = best_idx * rate / (len(spectrum) * 2)
            return peak_frequency, best

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

# Is not working, find more good algorithm
# Compare some sample and get sound range
class Process():

    def process_signal(buf1, buf2, buf3):
        max_signal_sample = []
        min_signal_sample = []
        for sig1, sig2, sig3 in zip(buf1, buf2, buf3):
            max_freq = max([sig1[0], sig2[0], sig3[0]])
            min_freq = min([sig1[0], sig2[0], sig3[0]])

        max_power = max([sig1[1], sig2[1], sig3[1]])
        min_power = min([sig1[1], sig2[1], sig3[1]])

        max_signal_sample.append((max_freq, max_power))
        min_signal_sample.append((min_freq, min_power))

        return max_signal_sample, min_signal_sample

