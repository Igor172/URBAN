import threading
import time

def write_words(word_count, file_name):
    with open('file_name', 'w') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


if __name__ == '__main__':
    time_start_1 = time.time()

    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

    time_stop_1 = time.time()
    print(f'Работа потоков {time_stop_1 - time_start_1}')

    time_start_2 = time.time()

    thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt',), daemon=True)
    thread_1.start()
    thread_1.join()
    thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt',), daemon=True)
    thread_2.start()
    thread_2.join()
    thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt',), daemon=True)
    thread_3.start()
    thread_3.join()
    thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt',), daemon=True)
    thread_4.start()
    thread_4.join()

    time_stop_2 = time.time()
    print(f'Работа потоков {time_stop_2 - time_start_2}')