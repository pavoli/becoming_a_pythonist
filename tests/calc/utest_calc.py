# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


import unittest
from tests.calc import calc


class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calc.sub(4, 1), 3)

    def test_mul(self):
        self.assertEqual(calc.mul(1, 3), 3)

    def test_div(self):
        self.assertEqual(calc.div(6, 2), 3)


if __name__ == '__main__':
    unittest.main()