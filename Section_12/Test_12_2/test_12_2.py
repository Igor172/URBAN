import unittest
from unittest import TestCase
import runner_and_tournament as rat


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rat.Runner('Усэйн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)

    def test_tour1(self):
        tour1 = rat.Tournament(90, self.runner1, self.runner3)
        result = tour1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn1'] = result

    def test_tour2(self):
        tour2 = rat.Tournament(90, self.runner2, self.runner3)
        result = tour2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn2'] = result

    def test_tour3(self):
        tour3 = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tour3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn3'] = result

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            for key, value in test_value.items():
                print(f'{key}: {value.name}')


if __name__ == '__main__':
    unittest.main()



















