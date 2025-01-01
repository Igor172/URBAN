import logging
import unittest
from rt_with_exceptions import Runner


logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner_1 = Runner('Athlet_1', -5)
            logging.info(f'"test_walk" выполнен успешно', exc_info=True)
            for _ in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
        except ValueError as err:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)


    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner_2 = Runner(2, 5)
            logging.info(f'"test_run" выполнен успешно', exc_info=True)
            for _ in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
        except TypeError as err:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)


    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_3 = Runner('Athlet_3')
        for _ in range(10):
            runner_3.run()
        runner_4 = Runner('Athlet_4')
        for _ in range(10):
            runner_4.walk()
        self.assertNotEqual(runner_3, runner_4, msg='Атлеты прошли разную дистанцию')


if __name__ == '__main__':

    unittest.main()


























