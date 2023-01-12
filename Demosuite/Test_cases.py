import CalcMode as cm
import unittest
print(cm.name)
print(cm.version)
class my_Test(unittest.TestCase):
    def test_add(self):
        result = cm.add_int(4,5)
        self.assertEqual(result,9)
    def test_mul(self):
        result = cm.mul(4,5)
        self.assertEqual(result,20)
    def test_sub(self):
        result = cm.sub(4,5)
        self.assertEqual(result,-1)
    def test_div(self):
        result = cm.div(10,10)
        self.assertEqual(result,1)