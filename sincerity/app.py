from .module import PyAudioInput, PyAudioData
import .controller as cl


def main():
    audio_data = PyAudioData(format=16, channels=1, rate=44100, chunk=1024)

    audio_input = PyAudioInput(audio_data)

    print('Recoding buf 1 until 3 sec ...')
    buf1 = get_signal_buffer(3)
    print('Recoding buf 2 until 3 sec ...')
    buf2 = get_signal_buffer(3)
    print('Recoding buf 3 until 3 sec ...')
    buf3 = get_signal_buffer(3)

    print('processing signal...')

    max_signal, min_signal = cl.process_signal(buf1, buf2, buf3)

    print('max signal result:')
    for signal in max_signal:
        max_log.write(' '.join(str(e) for e in signal) + '\n')

    print('min signal result:')
    for signal in min_signal:
        min_log.write(' '.join(str(e) for e in signal) + '\n')

    min_log.close()
    max_log.close()

if __name__ == '__main__':
    main()
