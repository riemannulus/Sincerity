import audioop
import pyaudio

class PyAudioInput():

    def __init__(self, pyaudiodata):
        self.p = pyaudiodata.p
        self.stream = self.p.open(
            format=pyaudiodata.format,
            channels=pyaudiodata.channels,
            rate=pyaudiodata.rate,
            input=True,
            frames_per_buffer=pyaudiodata.chunk)

    def read(self):
        data = self.stream.read(1024)
        samples = [audioop.getsample(data, 2, n)
                   for n in range(0, 1024)]
        return samples

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()

class PyAudioData():

    def __init__(self, format, channels, rate, chunk, input=True):
        self.p = pyaudio.PyAudio()
        if format == 8:
            self.format=pyaudio.paInt8
        elif format == 16:
            self.format=pyaudio.paInt16
        elif formant == 24:
            self.format=pyaudio.paInt24
        elif formant == 32:
            self.format=pyaudio.paInt32

        self.channels=channels
        self.rate=rate
        if input:
            self.input=True
        else:
            self.output=True
        self.chunk=chunk
