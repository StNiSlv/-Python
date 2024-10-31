from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days = 0
        print(f"{self.name}, на нас напали!")

        while enemies > 0:
            days += 1
            enemies -= self.power
            remaining_enemies = max(0, enemies)  # Количество оставшихся врагов не может быть меньше нуля
            print(f"{self.name} сражается {days} день(дня)..., осталось {remaining_enemies} воинов.")
            sleep(1)

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

# Создание объектов класса Knight
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения всех потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
