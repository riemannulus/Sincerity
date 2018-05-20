import pyaudio
import audioop

from module import *
from controller import *


def main():

    PIVOT_VOLUME = 10000000
    max_usr_buf = []
    min_usr_buf = []
    audio_data = PyAudioData(format=16, channels=1, rate=44100, chunk=1024)
    data_getter = DataGetter(audio_data)

    def get_data():

        print('Recoding buf 1 until 3 sec ...')
        buf1 = data_getter.get_signal_buffer(3)
        print('Recoding buf 2 until 3 sec ...')
        buf2 = data_getter.get_signal_buffer(3)
        print('Recoding buf 3 until 3 sec ...')
        buf3 = data_getter.get_signal_buffer(3)

        print('processing signal...')

        buf1 = process_signal(buf1, PIVOT_VOLUME)
        buf2 = process_signal(buf2, PIVOT_VOLUME)
        buf3 = process_signal(buf3, PIVOT_VOLUME)

        print('processing completed!')

        max_buf = get_highest_volume(buf1, buf2, buf3)
        min_buf = get_lowest_volume(buf1, buf2, buf3)

        for b in max_buf:
            max_log.write(' '.join(str(e) for e in b) + '\n')

        for b in min_buf:
            min_log.write(' '.join(str(e) for e in b) + '\n')

        print('Saving complelete!')

    def set_data():

        print('Set sound data from files')
        for line in max_log.readlines():
            strip_line = line.strip()
            max_usr_buf.append(strip_line.split(' '))

        for line in min_log.readlines():
            strip_line = line.strip()
            min_usr_buf.append(strip_line.split(' '))

        print(min_usr_buf)

    try:
        max_log=open('max_buffer.log', 'r')
        min_log=open('min_buffer.log', 'r')
        print('open complete!')

    except IOError:
        max_log=open('max_buffer.log', 'w')
        min_log=open('min_buffer.log', 'w')

        get_data()

        max_log.close()
        min_log.close()
        max_log=open('max_buffer.log', 'r')
        min_log=open('min_buffer.log', 'r')

    set_data()
    max_log.close()
    min_log.close()

if __name__ == '__main__':
    main()
