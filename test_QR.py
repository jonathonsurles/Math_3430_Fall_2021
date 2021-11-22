"""Tests functions in QR.py"""


import pytest
import QR
import LA


Test = tuple[tuple, object]  # The type that every Test will return for Demo


# Allowable margin for error for any tests that use it
MARGIN = .0001


def test_normalize() -> Test:
    """Tests QR.normalize()"""
    assert QR.normalize([4, 0, 0]) == [[1, 0, 0], 4]
    assert QR.normalize([1, 1, 1]) == [[1/3**.5, 1/3**.5, 1/3**.5], 3**.5]
    return ([4, 0, 0],), [[1, 0, 0], 4]


def test_orthagonalize() -> Test:
    """Tests QR.orthagonalize()"""
    assert QR.orthagonalize([1, 1], [0, 1]) == [[1, 0], 1]
    assert QR.orthagonalize([-2.5, -2.5], [1, 0]) == [[0, -2.5], -2.5]
    return ([-2.5, -2.5], [1, 0]), [[0, -2.5], -2.5]


def test_gram_schmidt() -> Test:
    """Tests QR.gram_schmidt()"""
    # Simple test with the identity
    # [[1, 0], [1, 1]] should produce Q=[[1, 0], [0, 1]] R=[[1, 0], [1, 1]
    assert QR.gram_schmidt([[1, 0], [1, 1]]) == [[[1, 0], [0, 1]],
                                                 [[1, 0], [1, 1]]]
    # Modified identity test
    # [[1, 0], [-3, -3]] should produce Q=[[1, 0], [0, -1] R=[[1, 0], [-3, 3]]
    assert QR.gram_schmidt([[1, 0], [-3, -3]]) == [[[1, 0], [0, -1]],
                                                   [[1, 0], [-3, 3]]]
    return ([[1, 0], [-3, -3]],), [[[1, 0], [0, 1]], [[1, 0], [1, 1]]]


def test_orthonormalize() -> Test:
    """Tests QR.orthonormalize()"""
    # Simple test with the identity
    # [[1, 0], [1, 1]] should produce [[1, 0], [0, 1]]
    assert QR.orthonormalize([[1, 0], [1, 1]]) == [[1, 0], [0, 1]]
    # Modified identity test
    # [[1, 0], [-3, -3]] should produce [[1, 0], [0, -1]
    assert QR.orthonormalize([[1, 0], [-3, -3]]) == [[1, 0], [0, -1]]
    return ([[1, 0], [-3, -3]],), [[1, 0], [0, -1]]


def test_householder() -> Test:
    """Tests QR.householder()"""
    # Yoinked from tests from the internet because I like nice numbers
    # Test from atozmath.com: QR Decomposition (Householder Method) ex. 1
    expected_q1 = [[-.5, -.5, -.5, -.5], [.5, -.5, -.5, .5],
                   [-.5, .5, -.5, .5], [-.5, -.5, .5, .5]]
    expected_r1 = [[-2, 0, 0, 0], [-3, -5, 0, 0], [-2, 2, -4, 0]]
    test_case_1 = [[1, 1, 1, 1], [-1, 4, 4, -1], [4, -2, 2, 0]]
    actual_1 = QR.householder(test_case_1)
    assert LA.matrix_margin(actual_1[0], expected_q1) < MARGIN
    assert LA.matrix_margin(actual_1[1], expected_r1) < MARGIN
    # Test from atozmath.com: QR Decomposition (Householder Method) ex. 2
    expected_q2 = [[-2/3, -2/3, -1/3], [2/3, -1/3, -2/3], [-1/3, 2/3, -2/3]]
    expected_r2 = [[-3, 0, 0], [0, -3, 0], [-12, 12, -6]]
    test_case_2 = [[2, 2, 1], [-2, 1, 2], [18, 0, 0]]
    actual_2 = QR.householder(test_case_2)
    assert LA.matrix_margin(actual_2[0], expected_q2) < MARGIN
    assert LA.matrix_margin(actual_2[1], expected_r2) < MARGIN
    return (test_case_1,), [expected_q1, expected_r1]


# Run tests if file is run directly
if __name__ == "__main__":
    pytest.main(['test_QR.py'])
