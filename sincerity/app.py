from module import PyAudioData
from controller import DataGetter
from controller import get_highest_volume, get_lowest_volume
from controller import process_signal


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

        for ele in max_buf:
            max_log.write(' '.join(str(e) for e in ele) + '\n')

        for ele in min_buf:
            min_log.write(' '.join(str(e) for e in ele) + '\n')

        print('Saving complelete!')

    def set_data():

        print('Set sound data from files')
        for line in max_log.readlines():
            strip_line = line.strip()
            max_usr_buf.append(tuple(strip_line.split(' ')))

        for line in min_log.readlines():
            strip_line = line.strip()
            min_usr_buf.append(tuple(strip_line.split(' ')))

        print(min_usr_buf)

    try:
        max_log = open('max_buffer.log', 'r')
        min_log = open('min_buffer.log', 'r')
        print('open complete!')

    except IOError:
        max_log = open('max_buffer.log', 'w')
        min_log = open('min_buffer.log', 'w')

        get_data()

        max_log.close()
        min_log.close()
        max_log = open('max_buffer.log', 'r')
        min_log = open('min_buffer.log', 'r')

    set_data()
    max_log.close()
    min_log.close()

    while(True):
        is_scope = False
        signal = data_getter.process_stream()
        if signal[1] < PIVOT_VOLUME:
            continue

        for min_signal, max_signal in zip(min_usr_buf, max_usr_buf):
            if min_signal < signal < max_signal:
                is_scope = True
            else:
                is_scope = False
                break

            signal = data_getter.process_stream()

        if is_scope:
            print('data is in the scope!')


if __name__ == '__main__':
    main()
