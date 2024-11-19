import threading
from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        string_in_file = file.readline()
        all_data.append(string_in_file)



if __name__ == '__main__':
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for name in filenames:
        thread_n = threading.Thread(target=read_info, args=(name,))
        thread_n.start()
    stop_time = time.time()
    print(f'Время выполнения с помощью многопоточности составило {stop_time - start_time}')


    start_time = time.time()
    with Pool(4) as p:
        multiproc = p.map(read_info, filenames)
    stop_time = time.time()
    print('Время выполнения с помощью многопроцессности составило: ', stop_time - start_time)


