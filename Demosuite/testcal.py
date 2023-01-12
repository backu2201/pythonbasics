import unittest
def count_days(n):
    if n in [1,3,5,7,8,10,12]:
        return 31
    elif n in [4,6,9,11]:
        return 30
    else:
        return 28
class my_Test(unittest.TestCase):
    def  test(self):
        n=2
        result = count_days(n)
        self.assertEqual(result,28)
