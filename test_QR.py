"""Tests functions in QR.py"""


import pytest
import QR


# Allowable margin for error for any tests that use it
MARGIN = .0001


def equals_with_error(arg_a: list | complex,
                      arg_b: list | complex,
                      margin: float) -> bool:
    """Tests if an item is equal to another within an allowable error range

    Employs recursion. If the arguments are iterable, compare each matching
    pair of elements in the arguments. Otherwise we have the base case, where
    we compare the absolute value of the difference between the each element
    (which we now know to be numbers) with the margin of error. If false, we
    break recursion and return false, but if we get through all elements, we
    return true.

    Args:
        arg_a: A list or a complex number to be compared.
        arg_b: A list or a complex number to be compared. Must be the same
          type as arg_a and if a list, must be the same length as arg_a

        margin: A floating point number, the allowable error by which the
                absolute value of the args can differ

    Returns:
        A boolean value, representing if the arguments are equal within the
        given allowable error range
    """
    # Iterable case: compare corresponding elements
    if hasattr(arg_a, '__iter__'):
        for var_a, var_b in zip(arg_a, arg_b):
            if not equals_with_error(var_a, var_b, margin):
                return False
    # Non-iterable case:
    else:
        if abs(arg_a - arg_b) > margin:
            return False
    return True


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
    expected_1 = [expected_q1, expected_r1]
    test_case_1 = [[1, 1, 1, 1], [-1, 4, 4, -1], [4, -2, 2, 0]]
    actual_1 = QR.householder(test_case_1)
    assert equals_with_error(actual_1, expected_1, MARGIN)
    # Test from atozmath.com: QR Decomposition (Householder Method) ex. 2
    expected_q2 = [[-2/3, -2/3, -1/3], [2/3, -1/3, -2/3], [-1/3, 2/3, -2/3]]
    expected_r2 = [[-3, 0, 0], [0, -3, 0], [-12, 12, -6]]
    expected_2 = [expected_q2, expected_r2]
    test_case_2 = [[2, 2, 1], [-2, 1, 2], [18, 0, 0]]
    actual_2 = QR.householder(test_case_2)
    assert equals_with_error(actual_2, expected_2, MARGIN)


# Run tests if file is run directly
if __name__ == "__main__":
    pytest.main(['test_QR.py'])
