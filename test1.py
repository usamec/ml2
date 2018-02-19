from solution import Variable
import unittest

class TestForward(unittest.TestCase):
    def test_value(self):
        a = Variable(47.0)
        self.assertAlmostEqual(a.value, 47.0)

    def test_plus(self):
        a = Variable(1.0)
        b = Variable(2.0)
        c = a + b
        self.assertAlmostEqual(a.value, 1.0)
        self.assertAlmostEqual(c.value, 3.0)

    def test_plus2(self):
        a = Variable(1.0)
        c = 2 + a
        self.assertAlmostEqual(a.value, 1.0)
        self.assertAlmostEqual(c.value, 3.0)
        

    def test_plus3(self):
        a = Variable(1.0)
        c = a + 2
        self.assertAlmostEqual(a.value, 1.0)
        self.assertAlmostEqual(c.value, 3.0)
        
    def test_minus(self):
        a = Variable(1.0)
        b = Variable(2.0)
        c = a - b
        self.assertAlmostEqual(a.value, 1.0)
        self.assertAlmostEqual(c.value, -1.0)

    def test_minus2(self):
        a = Variable(1.0)
        c = 2 - a
        self.assertAlmostEqual(a.value, 1.0)
        self.assertAlmostEqual(c.value, 1.0)
        

    def test_minus3(self):
        a = Variable(1.0)
        c = a - 2
        self.assertAlmostEqual(a.value, 1.0)
        self.assertAlmostEqual(c.value, -1.0)

    def test_mul(self):
        a = Variable(1.0)
        b = Variable(2.0)
        c = a * b
        self.assertAlmostEqual(a.value, 1.0)
        self.assertAlmostEqual(c.value, 2.0)

    def test_mul2(self):
        a = Variable(1.0)
        c = 2 * a
        self.assertAlmostEqual(a.value, 1.0)
        self.assertAlmostEqual(c.value, 2.0)
        

    def test_mul3(self):
        a = Variable(1.0)
        c = a * 2
        self.assertAlmostEqual(a.value, 1.0)
        self.assertAlmostEqual(c.value, 2.0)

    def test_expression(self):
        a = Variable(1.0)
        b = Variable(2.0)
        c = Variable(3.0)
        d = a * b + a * c + b * c
        e = 2.0 * (d * b - 5.0)
        self.assertAlmostEqual(d.value, 11.0)
        self.assertAlmostEqual(e.value, 34.0)

if __name__ == '__main__':
    unittest.main()
