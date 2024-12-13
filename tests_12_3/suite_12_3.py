import unittest
import tests_12_1
import tests_12_3

rutoTST = unittest.TestSuite()
rutoTST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
rutoTST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

run = unittest.TextTestRunner(verbosity=2)
run.run(rutoTST)