import unittest
def lon(l):
    for each in l:
        l.reverse()
    return l
class my_Test(unittest.TestCase):
    def test(self):
        l=["sai","madhu","chinnu"]
        r=lon(l)
        self.assertEqual(r,["chinnu","madhu","sai"])
