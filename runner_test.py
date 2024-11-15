import unittest
from runner_and_tournament import Runner, Tournament

def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return test_func(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner = Runner("Тестовый", speed=5)

    @skip_if_frozen
    def test_walk(self):
        for _ in range(10):
            self.runner.walk()
        self.assertEqual(self.runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        for _ in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Усэйн", speed=10)
        runner2 = Runner("Ник", speed=3)
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.assertEqual(results[2], self.runner3)

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.assertEqual(results[2], self.runner3)

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.assertEqual(results[3], self.runner3)
