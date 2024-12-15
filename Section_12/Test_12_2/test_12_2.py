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

    def tour1(self):
        tour1 = rat.Tournament(90, self.runner1, self.runner3)
        tour1.start()
        self.all_results.update(tour1.start())
        self.assertTrue(self.all_results[len(self.all_results) - 1] == 'Ник', 'Ник всегда должен быть последним')

    def tour2(self):
        tour2 = rat.Tournament(90, self.runner2, self.runner3)
        tour2.start()
        self.all_results.update(tour2.start())
        self.assertTrue(self.all_results[len(self.all_results) - 1] == 'Ник', 'Ник всегда должен быть последним')

    def tour3(self):
        tour3 = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        tour3.start()
        self.all_results.update(tour3.start())
        self.assertTrue(self.all_results[len(self.all_results) - 1] == 'Ник', 'Ник всегда должен быть последним')


    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            for el in value:
                print(el)


if __name__ == '__main__':
    unittest.main()



















