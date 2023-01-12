import unittest
def losr(l):
    for each in l:
        return l[::-1]
class my_Test(unittest.TestCase):
    def test(self):
        l=[1,2,"hello"]
        r=losr(l)
        self.assertEqual(r,["hello",2,1])