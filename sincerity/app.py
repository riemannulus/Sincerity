import pyaudio
import audioop

from module import *
from controller import *


def main():

    audio_data = PyAudioData(format=16, channels=1, rate=44100, chunk=1024)
    data_getter = DataGetter(audio_data)

    max_log=open('max_buffer.log', 'w')
    min_log=open('min_buffer.log', 'w')

    print('Recoding buf 1 until 3 sec ...')
    buf1 = data_getter.get_signal_buffer(3)
    print('Recoding buf 2 until 3 sec ...')
    buf2 = data_getter.get_signal_buffer(3)
    print('Recoding buf 3 until 3 sec ...')
    buf3 = data_getter.get_signal_buffer(3)

    print('processing signal...')

    max_buf = get_higest_volume(buf1, buf2, buf3)
    min_buf = get lowest_volume(buf1, buf2, buf3)

    print("""
          processing signal complete!
          """)

    print("""
          Saving buffer log
          """)

    for b in max_buf:
        max_log.write(' '.join(str(e) for e in b) + '\n')
    for b in min_buf:
        min_log.write(' '.join(str(e) for e in b) + '\n')

    max_log.close()
    min_log.close()

    print("""
          Saving complelete! program exterm
          """)

if __name__ == '__main__':
    main()
