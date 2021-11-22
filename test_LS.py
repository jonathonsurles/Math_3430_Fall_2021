"""Tests functions in LS.py."""


import pytest
import LS
import LA


Case = tuple[tuple, object]  # The type that every test will return for Demo


# Allowable margin for error for any tests that use it
MARGIN = .0001


def test_least_squares() -> Case:
    """Tests LS.least_squares()"""
    actual1 = LS.least_squares([[2, 0, 0], [4, 4, 0], [3, 1, 6]], [9, 5, 6])
    assert LA.vector_margin(actual1, [1, 1, 1]) < MARGIN
    actual2 = LS.least_squares([[1, 1, 1], [0, 1, 2]], [6, 0, 0])
    assert LA.vector_margin(actual2, [5, -3]) < MARGIN
    return ([[2, 0, 0], [4, 4, 0], [3, 1, 6]], [9, 5, 6]), [1, 1, 1]


if __name__ == '__main__':
    pytest.main(['test_LS.py'])
