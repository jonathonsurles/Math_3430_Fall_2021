"""Tests functions in LS.py."""


import pytest
import LS
import LA


# Allowable margin for error for any tests that use it
MARGIN = .0001
# Lambdas for margin of error comparison
vector_margin = lambda v1, v2 : LA.p_norm(LA.add_vectors(
        LA.vector_scalar_multiply(v1, -1), v2))
matrix_margin = lambda m1, m2 : LA.p_q_norm(LA.matrix_add(
        LA.matrix_scalar_multiply(m1, -1), m2))


def test_least_squares():
    """Tests LS.least_squares()"""
    actual1 = LS.least_squares([[2, 0, 0], [4, 4, 0], [3, 1, 6]], [9, 5, 6])
    assert vector_margin(actual1, [1, 1, 1]) < MARGIN
    actual2 = LS.least_squares([[1, 1, 1], [0, 1, 2]], [6, 0, 0])
    assert vector_margin(actual2, [5, -3]) < MARGIN


if __name__ == '__main__':
    pytest.main(['test_LS.py'])
