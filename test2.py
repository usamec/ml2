from solution import Variable
import unittest
from math import exp, log, tanh

class TestForward(unittest.TestCase):
    def test_div(self):
        a = Variable(1.0)
        b = Variable(2.0)
        c = a / b
        self.assertAlmostEqual(a.value, 1.0)
        self.assertAlmostEqual(c.value, 0.5)

    def test_div2(self):
        a = Variable(1.0)
        c = 2 / a
        self.assertAlmostEqual(a.value, 1.0)
        self.assertAlmostEqual(c.value, 2.0)
        

    def test_div3(self):
        a = Variable(1.0)
        c = a / 2
        self.assertAlmostEqual(a.value, 1.0)
        self.assertAlmostEqual(c.value, 0.5)

    def test_exp(self):
        a = Variable(1.5)
        c = a.exp()
        self.assertAlmostEqual(c.value, exp(1.5))

    def test_log(self):
        a = Variable(1.5)
        c = a.log()
        self.assertAlmostEqual(c.value, log(1.5))

    def test_tanh(self):
        a = Variable(1.5)
        c = a.tanh()
        self.assertAlmostEqual(c.value, tanh(1.5))

    def test_tanh2(self):
        a = Variable(0)
        c = a.tanh()
        self.assertAlmostEqual(c.value, 0.0)
     
    def test_expression(self):
        a = Variable(0.0)
        p = 1.0 / (1 + (-3*a).exp())
        self.assertAlmostEqual(p.value, 0.5)
        loss = p.log()
        self.assertAlmostEqual(loss.value, log(0.5))

        a2 = Variable(1.0)
        p2 = 1.0 / (1 + (-3*a2).exp())
        self.assertAlmostEqual(p2.value, 0.952574126)
        loss2 = p2.log()
        self.assertAlmostEqual(loss2.value, log(0.952574126))


class TestDerivatives(unittest.TestCase):
    def test_div(self):
        a = Variable(1.0)
        b = Variable(2.0)
        c = a / b
        c.backward()
        self.assertAlmostEqual(a.d.value, 0.5)
        self.assertAlmostEqual(b.d.value, -0.25)

    def test_div2(self):
        a = Variable(1.0)
        c = 2 / a
        c.backward()
        self.assertAlmostEqual(a.d.value, -2.0)
        

    def test_div3(self):
        a = Variable(1.0)
        c = a / 2
        c.backward()
        self.assertAlmostEqual(a.d.value, 0.5)

    def test_exp(self):
        a = Variable(1.5)
        c = a.exp()
        c.backward()
        self.assertAlmostEqual(c.value, exp(1.5))
        self.assertAlmostEqual(a.d.value, exp(1.5))

    def test_log(self):
        a = Variable(1.5)
        c = a.log()
        c.backward()
        self.assertAlmostEqual(c.value, log(1.5))
        self.assertAlmostEqual(a.d.value, 1/1.5)

    def test_tanh(self):
        a = Variable(1.5)
        c = a.tanh()
        c.backward()
        self.assertAlmostEqual(a.d.value, 1-tanh(1.5)**2)

    def test_tanh2(self):
        a = Variable(0)
        c = a.tanh()
        c.backward()
        self.assertAlmostEqual(a.d.value, 1.0)

    def test_expression(self):
        a = Variable(0.0)
        p = 1.0 / (1 + (-3*a).exp())
        self.assertAlmostEqual(p.value, 0.5)
        loss = p.log()
        self.assertAlmostEqual(loss.value, log(0.5))
        loss.backward()
        self.assertAlmostEqual(a.d.value, 1.5)

        a2 = Variable(1.0)
        p2 = 1.0 / (1 + (-3*a2).exp())
        self.assertAlmostEqual(p2.value, 0.952574126)
        loss2 = p2.log()
        self.assertAlmostEqual(loss2.value, log(0.952574126))
        loss2.backward()
        self.assertAlmostEqual(a2.d.value, (1-0.952574126)*3)


if __name__ == '__main__':
    unittest.main()
