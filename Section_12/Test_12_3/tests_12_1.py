import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name



class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = Runner('Athlet_1')
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50) #Намеренно ввели бОльшее значение чем ожидалось, тесты показали место ошибки

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = Runner('Athlet_2')
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

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






















