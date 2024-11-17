import random
import time
import threading

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        transactions_lim = 100
        for i in range(transactions_lim):
            summ = random.randint(50, 500)
            self.balance += summ
            print(f'Пополнение {summ}. Баланс {self.balance}')
        if self.balance >= 500 and self.lock.locked() == True:
            self.lock.release()
        time.sleep(0.001)

    def take(self):
        transactions_lim = 100
        for i in range(transactions_lim):
            summ = random.randint(50, 500)
            print(f'Запрос на {summ}')
            if summ <= self.balance:
                self.balance -= summ
                print(f'Снятие: {summ}. Баланс: {self.balance}')
            elif summ > self.balance:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()



if __name__ == '__main__':
    bk = Bank()

    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')






