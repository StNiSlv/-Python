import threading
import time
import random
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number  # номер стола
        self.guest = None  # текущий гость за столом (по умолчанию None)

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name  # имя гостя

    def run(self):
        # Симуляция приема пищи, ожидание от 3 до 10 секунд
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)  # столы в кафе
        self.queue = Queue()  # очередь гостей

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                free_table.guest = guest  # посадка гостя за свободный стол
                guest.start()  # запуск потока гостя
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)  # добавление гостя в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    # Гость закончил прием пищи
                    print(f"{table.guest.name} покушал(-а) и ушел(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # освобождаем стол

                if table.guest is None and not self.queue.empty():
                    # Пересаживаем гостя из очереди
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    next_guest.start()  # запуск потока нового гостя
            time.sleep(0.5)  # небольшая задержка, чтобы имитировать обслуживание

# Пример использования
tables = [Table(1), Table(2), Table(3)]  # создаем три стола
cafe = Cafe(*tables)

# Создаем гостей
guests = [Guest("Вася"), Guest("Петя"), Guest("Маша"), Guest("Оля"), Guest("Саша")]

# Запускаем прибытие гостей и обслуживание
cafe.guest_arrival(*guests)
cafe.discuss_guests()
