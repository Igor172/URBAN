from multiprocessing import Pool
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            string_in_file = file.readline()
            all_data.append(string_in_file)
            if not string_in_file:
                break


if __name__ == '__main__':
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for name in filenames:
        read_info(name)            #Запускаем функцию 4 раза и обрабатываем наши файлы поочередно одним потоком MainThread
    stop_time = time.time()
    print(f'Время выполнения с помощью многопоточности составило {stop_time - start_time}')



    start_time = time.time()
    with Pool(4) as p:
        multiproc = p.map(read_info, filenames)
    stop_time = time.time()
    print('Время выполнения с помощью многопроцессности составило: ', stop_time - start_time)