import time

from numpy import mean, std
from numpy.fft import fft


def get_peak_frequency(spectrum, rate):
    best = -1
    best_idx = 0
    for n in range(len(spectrum)):
        if abs(spectrum[n]) > best:
            best = abs(spectrum[n])
            best_idx = n

    peak_frequency = best_idx * rate / (len(spectrum) * 2)
    return peak_frequency, best

def get_spectrum(samples):
    result = fft(samples)
    return result[:int(len(result)/2)]

def get_signal_buffer(end_gap):
    input = PyAudioInput()
    start_time = time.time()
    buffer = []

    while(True):
        samples = input.read()
        if not len(samples):
            continue

        spectrum = get_spectrum(samples)
        freq = get_peak_frequency(spectrum, RATE)

        now = time.time()
        buffer.append(freq)
        if now - start_time > end_gap:
            return buffer


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

