"""Tests functions in QR.py"""


import pytest
import QR


def equals_with_error(arg_a, arg_b, allowable_error):
    """Tests if an item is equal to another within an allowable error range"""
    # Check if the args are iterable
    if hasattr(arg_a, '__iter__'):
        for a, b in zip(arg_a, arg_b):
            if not equals_with_error(a, b, allowable_error):
                return False
    else:
        if abs(arg_a - arg_b) > allowable_error:
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


def test_gram_schmidt_unstable():
    """Tests QR.gram_schmidt_unstable()"""
    # Simple test with the identity
    # [[1, 0], [1, 1]] should produce Q=[[1, 0], [0, 1]] R=[[1, 0], [1, 1]
    assert QR.gram_schmidt_unstable([[1, 0], [1, 1]]) == [[[1, 0], [0, 1]],
                                                          [[1, 0], [1, 1]]]
    # Modified identity test
    # [[1, 0], [-3, -3]] should produce Q=[[1, 0], [0, -1] R=[[1, 0], [-3, 3]]
    assert QR.gram_schmidt_unstable([[1, 0], [-3, -3]]) == [[[1, 0], [0, -1]],
                                                            [[1, 0], [-3, 3]]]

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


def test_householder_orth():
    """Tests QR.householder_orth()"""
    # Tests from atozmath.com
    test_case_1 = [[1, 1, 1, 1], [-1, 4, 4, -1], [4, -2, 2, 0]]
    expected_q1 = [[-.5, -.5, -.5, -.5], [.5, -.5, -.5, .5], [-.5, .5, -.5, .5], [-.5, -.5, .5, .5]]
    expected_r1 = [[-2, 0, 0, 0], [-3, -5, 0, 0], [-2, 2, -4, 0]]
    assert equals_with_error(QR.householder_orth(test_case_1), [expected_q1, expected_r1], .0001)
    test_case_2 = [] 


# Run tests if file is run directly
if __name__ == "__main__":
    pytest.main(['test_QR.py'])
