import unittest
from runner_test import RunnerTest, TournamentTest

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
