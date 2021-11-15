"""Tests functions in QR.py"""


import pytest
import QR
import LA


# Allowable margin for error for any tests that use it
MARGIN = .0001
# Lambdas for margin of error comparison
vector_margin = lambda v1, v2 : LA.p_norm(LA.add_vectors(
        LA.vector_scalar_multiply(v1, -1), v2))
matrix_margin = lambda m1, m2 : LA.p_q_norm(LA.matrix_add(
        LA.matrix_scalar_multiply(m1, -1), m2))


def test_normalize():
    """Tests QR.normalize()"""
    assert QR.normalize([4, 0, 0]) == [[1, 0, 0], 4]
    assert QR.normalize([1, 1, 1]) == [[1/3**.5, 1/3**.5, 1/3**.5], 3**.5]


def test_orthagonalize():
    """Tests QR.orthagonalize()"""
    assert QR.orthagonalize([1, 1], [0, 1]) == [[1, 0], 1]
    assert QR.orthagonalize([-2.5, -2.5], [1, 0]) == [[0, -2.5], -2.5]


def test_gram_schmidt():
    """Tests QR.gram_schmidt()"""
    # Simple test with the identity
    # [[1, 0], [1, 1]] should produce Q=[[1, 0], [0, 1]] R=[[1, 0], [1, 1]
    assert QR.gram_schmidt([[1, 0], [1, 1]]) == [[[1, 0], [0, 1]],
                                                 [[1, 0], [1, 1]]]
    # Modified identity test
    # [[1, 0], [-3, -3]] should produce Q=[[1, 0], [0, -1] R=[[1, 0], [-3, 3]]
    assert QR.gram_schmidt([[1, 0], [-3, -3]]) == [[[1, 0], [0, -1]],
                                                   [[1, 0], [-3, 3]]]


def test_orthonormalize():
    """Tests QR.orthonormalize()"""
    # Simple test with the identity
    # [[1, 0], [1, 1]] should produce [[1, 0], [0, 1]]
    assert QR.orthonormalize([[1, 0], [1, 1]]) == [[1, 0], [0, 1]]
    # Modified identity test
    # [[1, 0], [-3, -3]] should produce [[1, 0], [0, -1]
    assert QR.orthonormalize([[1, 0], [-3, -3]]) == [[1, 0], [0, -1]]


def test_householder():
    """Tests QR.householder()"""
    # Yoinked from tests from the internet because I like nice numbers
    # Test from atozmath.com: QR Decomposition (Householder Method) ex. 1
    expected_q1 = [[-.5, -.5, -.5, -.5], [.5, -.5, -.5, .5],
                   [-.5, .5, -.5, .5], [-.5, -.5, .5, .5]]
    expected_r1 = [[-2, 0, 0, 0], [-3, -5, 0, 0], [-2, 2, -4, 0]]
    test_case_1 = [[1, 1, 1, 1], [-1, 4, 4, -1], [4, -2, 2, 0]]
    actual_1 = QR.householder(test_case_1)
    assert matrix_margin(actual_1[0], expected_q1) < MARGIN
    assert matrix_margin(actual_1[1], expected_r1) < MARGIN
    # Test from atozmath.com: QR Decomposition (Householder Method) ex. 2
    expected_q2 = [[-2/3, -2/3, -1/3], [2/3, -1/3, -2/3], [-1/3, 2/3, -2/3]]
    expected_r2 = [[-3, 0, 0], [0, -3, 0], [-12, 12, -6]]
    test_case_2 = [[2, 2, 1], [-2, 1, 2], [18, 0, 0]]
    actual_2 = QR.householder(test_case_2)
    assert matrix_margin(actual_2[0], expected_q2) < MARGIN
    assert matrix_margin(actual_2[1], expected_r2) < MARGIN


# Run tests if file is run directly
if __name__ == "__main__":
    pytest.main(['test_QR.py'])
