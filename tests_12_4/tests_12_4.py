import rt_with_exceptions
import unittest
import logging

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='utf-8',
                        format='%(asctime)s – [%(levelname)s] | %(message)s')

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_r = rt_with_exceptions.Runner('tst', -10)
            for i in range(10):
                test_r.walk()
            self.assertEqual(test_r.distance, 50)
            logging.info('test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_r = rt_with_exceptions.Runner(50)
            for i in range(10):
                test_r.run()
            self.assertEqual(test_r.distance, 100)
            logging.info('test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_r_1 = rt_with_exceptions.Runner('tst_1')
        test_r_2 = rt_with_exceptions.Runner('tst_2')
        for i in range(10):
            test_r_1.run()
            test_r_2.walk()
        self.assertNotEqual(test_r_1.distance, test_r_2.distance)

if __name__ == '__main__':
    unittest.main()