import unittest
import tests_12_1
import test_12_2


r_a_t_ST = unittest.TestSuite()

r_a_t_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
r_a_t_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(r_a_t_ST)


