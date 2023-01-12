import unittest
from Test_cases import my_Test
from test_sai import my_Test
from Test_case import my_Test
def my_suite():
    suite=unittest.TestSuite()
    r=unittest.TestResult()
    suite.addTests(unittest.makeSuite(my_Test))
    suite.addTests(unittest.makeSuite(my_Test))
    suite.addTests(unittest.makeSuite(my_Test))
    runner=unittest.TextTestRunner(verbosity=2)
    print(runner.run(suite))
my_suite()