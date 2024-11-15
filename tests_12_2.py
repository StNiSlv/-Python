import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", speed=10)
        self.runner_andrey = Runner("Андрей", speed=9)
        self.runner_nik = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        print("Все результаты тестов:")
        for test_num, results in cls.all_results.items():
            print(f"Тест {test_num}: {results}")

    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        results = tournament.start()
        self.__class__.all_results[1] = {place: str(runner) for place, runner in results.items()}
        self.assertEqual(results[2], self.runner_nik)

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nik)
        results = tournament.start()
        self.__class__.all_results[2] = {place: str(runner) for place, runner in results.items()}
        self.assertEqual(results[2], self.runner_nik)

    def test_race_all_runners(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nik)
        results = tournament.start()
        self.__class__.all_results[3] = {place: str(runner) for place, runner in results.items()}
        self.assertEqual(results[3], self.runner_nik)


if __name__ == "__main__":
    unittest.main()
