import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Test", speed=-10)
            runner.walk()
            self.assertEqual(runner.distance, -10)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", str(e))

    def test_run(self):
        try:
            runner = Runner(123, speed=10)
            runner.run()
            self.assertEqual(runner.distance, 20)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", str(e))

if __name__ == "__main__":
    unittest.main()
