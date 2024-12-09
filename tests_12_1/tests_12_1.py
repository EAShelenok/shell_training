import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_r = runner.Runner('tst')
        for i in range(10):
            test_r.walk()
        self.assertEqual(test_r.distance, 50)

    def test_run(self):
        test_r = runner.Runner('tst')
        for i in range(10):
            test_r.run()
        self.assertEqual(test_r.distance, 100)

    def test_challenge(self):
        test_r_1 = runner.Runner('tst_1')
        test_r_2 = runner.Runner('tst_2')
        for i in range(10):
            test_r_1.run()
            test_r_2.walk()
        self.assertNotEqual(test_r_1.distance, test_r_2.distance)

if __name__ == '__main__':
    unittest.main()