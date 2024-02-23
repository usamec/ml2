from solution import Variable
import unittest
from math import exp, log, tanh


class TestLong(unittest.TestCase):
    def test_long(self):
        a = Variable(1.0)
        b = Variable(1.0)
        cur_a = a
        cur_b = b
        for _ in range(50):
            new_a = (cur_a + cur_b) / 2
            new_b = (cur_a + cur_b) / 2
            cur_a = new_a
            cur_b = new_b

        out = cur_a + cur_b
        out.backward()
        self.assertAlmostEqual(a.d.value, 1)

if __name__ == "__main__":
    unittest.main()
