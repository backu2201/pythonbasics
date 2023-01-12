import unittest
def sum(a,b):
    return a+b
class my_Test(unittest.TestCase):
    def test(self):
        a=10
        b=20
        r=sum(a,b)
        self.assertEqual(r,30)