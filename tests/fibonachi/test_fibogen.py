# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


from tests.fibonachi import fibogen
import pytest


class TestFibogen:

    def test_type_error(self):
        with pytest.raises(TypeError):
            list(fibogen('trololo'))

    def test_negative(self):
        assert (list(fibogen(-1)) == [])

    def test_empty(self):
        assert (list(fibogen(0)) == [])

    def test_one(self):
        assert (list(fibogen(1)) == [1])

    def test_two(self):
        assert (list(fibogen(2)) == [1, 1])

    def test_three(self):
        assert (list(fibogen(3)) == [1, 1, 2])

    def test_seven(self):
        result = list(fibogen(7))
        expected = [1, 1, 2, 3, 5, 8, 13]
        assert (result == expected)

    @pytest.mark.randomize(num=int, min_num=3, max_num=1000, ncalls=99)
    def test_quickcheck(self, num):
        result = list(fibogen(num))
        assert (result[0] < result[-1])
        assert (len(result) == num)