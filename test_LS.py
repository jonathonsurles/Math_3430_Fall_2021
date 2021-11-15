"""Tests functions in LS.py."""


import pytest
import LS


def test_least_squares():
    """Tests LS.least_squares()"""
    assert LS.least_squares([[2, 0, 0], [4, 4, 0], [3, 1, 6]], [9, 5, 6]) \
            == [1, 1, 1]
    assert LS.least_squares([[1, 1, 1], [0, 1, 2]], [6, 0, 0]) == [5, -3]


if __name__ == '__main__':
    pytest.main(['test_LS.py'])
