import unittest
def login(us,pw):
    if(us=="hcluser" and pw=="1234"):
        return 1
    else:
        return 0
class my_Test(unittest.TestCase):
    def test1(self):
        us="hcluser"
        pw="1234"
        r=login(us,pw)
        self.assertEqual(r,1)
    def test2(self):
        us="hcluser"
        pw="7896"
        r=login(us,pw)
        self.assertEqual(r,0)