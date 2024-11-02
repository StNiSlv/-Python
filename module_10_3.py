import threading
import random
import time
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            self.lock.acquire()
            try:
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
            finally:
                self.lock.release()
            # Проверка разблокировки при балансе >= 500
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)
    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            self.lock.acquire()
            try:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    # Блокируем поток при недостаточном балансе
                    if not self.lock.locked():
                        self.lock.acquire()
            finally:
                self.lock.release()
            time.sleep(0.001)
bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')

