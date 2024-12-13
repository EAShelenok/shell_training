import unittest
import runner_and_tournament

class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    #@unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.test_t_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.test_t_2 = runner_and_tournament.Runner('Андрей', 9)
        self.test_t_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for k in dict(sorted(cls.all_results.items())).keys():
            print(cls.all_results[k])

    # Усэйн и Ник
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tornament_un(self):
        tst_1 = runner_and_tournament.Tournament(90, self.test_t_1, self.test_t_3)
        self.all_results[1] = {k: str(v) for k, v in tst_1.start().items()}
        self.assertTrue(self.all_results[1][2] == self.test_t_3)

    # Андрей и Ник
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tornament_an(self):
        tst_2 = runner_and_tournament.Tournament(90, self.test_t_2, self.test_t_3)
        self.all_results[2] = {k: str(v) for k, v in tst_2.start().items()}
        self.assertTrue(self.all_results[2][2] == self.test_t_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tornament_uan(self):
        tst_3 = runner_and_tournament.Tournament(90, self.test_t_1, self.test_t_2, self.test_t_3)
        self.all_results[3] = {k: str(v) for k, v in tst_3.start().items()}
        self.assertTrue(self.all_results[3][3] == self.test_t_3)

if __name__ == '__main__':
    unittest.main()