import unittest, calc
class my_Test(unittest.TestCase):
    def Test(self):

        self.assertEqual(calc.add(10, 5), 15)
    def test(self):
        r=calc.add(10,5)
        self.assertEqual(r,15)
    def test1(self):
        r=calc.add(-2,-3)
        self.assertEqual(r,-5)
    def test2(self):
        r=calc.add(8, 9)
        self.assertEqual(r,17)
