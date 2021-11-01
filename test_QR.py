"""Tests functions in QR.py"""


from typing import Union
import pytest
import QR


def equals_with_error(arg_a: Union[list, complex],  # Py 3.10: list | complex
                      arg_b: Union[list, complex],  # Py 3.10: list | complex
                      allowable_error: float) -> bool:
    """Tests if an item is equal to another within an allowable error range

    If the arguments are iterable, recursively check each argument. Otherwise,
    take the absolute value of the difference of the arguments. If the
    absolute value is greater than the allowable error, return false,
    otherwise continue with execution and if all elements are good return
    true.

    Args:
        arg_a, arg_b: Lists or complex numbers to be compared. Must be the
                      same dimensions if lists.
        allowable_error: A floating point number, the allowable margin
                         by which the absolute value of the args can differ

    Returns:
        A boolean value, representing if the arguments are equal within the
        given allowable error range
    """
    # Check if the args are iterable
    if hasattr(arg_a, '__iter__'):
        for var_a, var_b in zip(arg_a, arg_b):
            if not equals_with_error(var_a, var_b, allowable_error):
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
    # Test from atozmath.com: QR Decomposition (Householder Method) ex. 1
    expected_q1 = [[-.5, -.5, -.5, -.5], [.5, -.5, -.5, .5],
                   [-.5, .5, -.5, .5], [-.5, -.5, .5, .5]]
    expected_r1 = [[-2, 0, 0, 0], [-3, -5, 0, 0], [-2, 2, -4, 0]]
    expected_1 = [expected_q1, expected_r1]
    test_case_1 = [[1, 1, 1, 1], [-1, 4, 4, -1], [4, -2, 2, 0]]
    actual_1 = QR.householder_orth(test_case_1)
    assert equals_with_error(actual_1, expected_1, .0001)
    # Test from atozmath.com: QR Decomposition (Householder Method) ex. 2
    expected_q2 = [[-2/3, -2/3, -1/3], [2/3, -1/3, -2/3], [-1/3, 2/3, -2/3]]
    expected_r2 = [[-3, 0, 0], [0, -3, 0], [-12, 12, -6]]
    expected_2 = [expected_q2, expected_r2]
    test_case_2 = [[2, 2, 1], [-2, 1, 2], [18, 0, 0]]
    actual_2 = QR.householder_orth(test_case_2)
    assert equals_with_error(actual_2, expected_2, .0001)


# Run tests if file is run directly
if __name__ == "__main__":
    pytest.main(['test_QR.py'])
