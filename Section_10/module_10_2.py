import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        counter = 0
        while enemies:
            time.sleep(1)
            enemies -= self.power
            counter += 1
            print(f'{self.name} сражается {counter} дней(дня)..., осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {counter} дней(дня)!')


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print('Все битвы закончились!')