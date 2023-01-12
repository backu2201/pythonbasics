import unittest
def mul(a,b):
    return a*b
class my_Test(unittest.TestCase):
    def test(self):
        a=10
        b=20
        r=mul(a,b)
        self.assertEqual(r,200)

    def test1(self):
        a=9
        b=9
        r=mul(a,b)
        self.assertEqual(r,81)

    def test2(self):
        a = 4
        b = 9
        r = mul(a, b)
        self.assertEqual(r, 36)

    def test3(self):
        a = 8
        b = 9
        r = mul(a, b)
        self.assertEqual(r, 72)
    def test4(self):
        a = 8
        b = 10
        r = mul(a, b)
        self.assertEqual(r, 80)

    def test5(self):
        a = 2
        b = 9
        r = mul(a, b)
        self.assertEqual(r, 18)



