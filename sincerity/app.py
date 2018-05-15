import pyaudio
import audioop

from module import *
from controller import *


def main():

    audio_data = PyAudioData(format=16, channels=1, rate=44100, chunk=1024)
    data_getter = DataGetter(audio_data)

    buf1_log=open('buf1.log', 'w')
    buf2_log=open('buf2.log', 'w')
    buf3_log=open('buf3.log', 'w')

    print('Recoding buf 1 until 3 sec ...')
    buf1 = data_getter.get_signal_buffer(3)
    print('Recoding buf 2 until 3 sec ...')
    buf2 = data_getter.get_signal_buffer(3)
    print('Recoding buf 3 until 3 sec ...')
    buf3 = data_getter.get_signal_buffer(3)

    print('processing signal...')

    for b in buf1:
        buf1_log.write(' '.join(str(e) for e in b) + '\n')
    for b in buf2:
        buf2_log.write(' '.join(str(e) for e in b) + '\n')
    for b in buf2:
        buf3_log.write(' '.join(str(e) for e in b) + '\n')

    buf1_log.close()
    buf2_log.close()
    buf3_log.close()

if __name__ == '__main__':
    main()
