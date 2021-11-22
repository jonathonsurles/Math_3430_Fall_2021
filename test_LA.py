"""Tests functions in LA.py."""


import pytest
import LA


# Test variables for all functions
SCALAR_A = 4
SCALAR_B = 7
SCALAR_C = 1j
SCALAR_D = 3+4j
vector_a = [1, 2, 4]
vector_b = [3, 1, 2]
vector_c = [5, 0, 3]
vector_d = [-9-6j, 5j, 8-1j]
matrix_a = [[1, 8, 4], [8, 7, 6], [3, 0, 9]]
matrix_b = [[5, 6, 2], [1, 7, 0], [4, 7, 7]]
matrix_c = [[5, 8, 6], [0, 5, 2], [9, 4, 3]]
matrix_d = [[-4-7j, 6-8j, -5j], [2+9j, 3-4j, 6+2j], [-5+3j, -1+7j, -1+2j]]


Case = tuple[tuple, object]  # The type that every test will return for Demo


def test_add_vectors() -> Case:
    """Tests the function LA.add_vectors()
    """
    tst_1 = (vector_a, vector_b)
    exp_1 = [4, 3, 6]
    assert LA.add_vectors(tst_1[0], tst_1[1]) == exp_1
    tst_2 = (vector_b, vector_d)
    exp_2 = [-6-6j, 1+5j, 10-1j]
    assert LA.add_vectors(tst_2[0], tst_2[1]) == exp_2
    return tst_1, exp_1


def test_vector_scalar_multiply() -> Case:
    """Tests the function LA.vector_scalar_multiply()"""
    # Test for real integers
    result_1 = [4, 8, 16]
    assert LA.vector_scalar_multiply(vector_a, SCALAR_A) == result_1
    # Test for complex "integers"
    result_2 = [6-9j, -5, 1+8j]
    assert LA.vector_scalar_multiply(vector_d, SCALAR_C) == result_2
    return (vector_a, SCALAR_A), result_1


def test_matrix_scalar_multiply() -> Case:
    """Tests the function LA.matrix_scalar_multiply()"""
    # Test for real integers
    result_1 = [[4, 32, 16], [32, 28, 24], [12, 0, 36]]
    assert LA.matrix_scalar_multiply(matrix_a, SCALAR_A) == result_1
    # Test for complex "integers"
    result_2 = [[7-4j, 8+6j, 5], [-9+2j, 4+3j, -2+6j], [-3-5j, -7-1j, -2-1j]]
    assert LA.matrix_scalar_multiply(matrix_d, SCALAR_C) == result_2
    return (matrix_a, SCALAR_A), result_1


def test_matrix_add() -> Case:
    """Tests the function LA.matrix_add()"""
    # Test for real integers
    result_1 = [[6, 14, 6], [9, 14, 6], [7, 7, 16]]
    assert LA.matrix_add(matrix_a, matrix_b) == result_1
    # Test for complex "integers"
    result_2 = [[1-7j, 12-8j, 2-5j], [3+9j, 10-4j, 6+2j], [-1+3j, 6+7j, 6+2j]]
    assert LA.matrix_add(matrix_b, matrix_d) == result_2
    return (matrix_a, matrix_b), result_1


def test_matrix_vector_multiply() -> Case:
    """Tests the function LA.matrix_vector_multiply()"""
    # Test 1 for real integers
    result_1 = [29, 22, 52]
    assert LA.matrix_vector_multiply(matrix_a, vector_a) == result_1
    # Test 2 for real integers
    result_2 = [24, 39, 20]
    assert LA.matrix_vector_multiply(matrix_b, vector_b) == result_2
    return (matrix_a, vector_a), result_1


def test_matrix_multiply() -> Case:
    """Tests the function LA.matrix_multiply()"""
    # Test 1 for real integers
    result_1 = [[59, 82, 74], [57, 57, 46], [81, 81, 121]]
    assert LA.matrix_multiply(matrix_a, matrix_b) == result_1
    # Test 2 for real integers
    result_2 = [[57, 128, 52], [13, 49, 14], [61, 103, 39]]
    assert LA.matrix_multiply(matrix_b, matrix_c) == result_2
    return (matrix_a, matrix_b), result_1


def test_abs_value() -> Case:
    """Tests the function LA.abs_value()"""
    # Test for negative float
    assert LA.abs_value(-3.4) == 3.4
    # Test for zero
    assert LA.abs_value(0) == 0
    # Test for positive integer
    assert LA.abs_value(4) == 4
    # Test for complex float
    assert LA.abs_value(3-4j) == 5.0
    return (3-4j,), 5.0


def test_p_norm_finite() -> Case:
    """Tests the function LA.p_norm_finite()"""
    # Test for real vector, euclidian norm
    assert LA.p_norm_finite([3, 4]) == 5.0
    assert LA.p_norm_finite([5, 3+4j], p=1) == 10.0
    return ([3, 4],), 5.0


def test_inf_norm() -> Case:
    """Tests the function LA.inf_norm()"""
    # Test for real vector
    assert LA.inf_norm([3, 4]) == 4.0
    # Test for complex vector
    assert LA.inf_norm([3, 3+4j]) == 5.0
    return ([3, 4],), 4.0


def test_p_norm() -> Case:
    """Tests the function LA.p_norm()"""
    # Repeats the tests from test_p_norm_finite and test_inf_norm
    assert LA.p_norm([3, 4]) == 5.0
    assert LA.p_norm([5, 3+4j], p=1) == 10.0
    assert LA.p_norm([3, 4], inf=True) == 4.0
    assert LA.p_norm([3, 3+4j], inf=True) == 5.0
    return ([3, 4],), 10.0


def test_p_q_norm() -> Case:
    """Tests the function LA.p_q_norm()"""
    assert LA.p_q_norm([[0, 0], [0, 0]]) == 0
    assert LA.p_q_norm([[3, 4], [5, 12]]) == 18
    return ([[3, 4], [5, 12]],), 18


def test_inner_product() -> Case:
    """Tests the function LA.inner_product()"""
    # Test for real vectors
    assert LA.inner_product(vector_a, vector_b) == 13
    # Test for complex vectors: <real, complex>
    assert LA.inner_product(vector_c, vector_d) == -21-33j
    # Test for complex vectors: <complex, real>
    assert LA.inner_product(vector_d, vector_c) == -21+33j
    return (vector_a, vector_b), 13


def test_conj_tpse() -> Case:
    """Tests the function LA.conj_tpse()"""
    test_1 = [[1, 3+3j], [-5, -5-2j]]
    expect_1 = [[1, -5], [3-3j, -5+2j]]
    assert LA.conj_tpse(test_1) == expect_1
    test_2 = [[-5, 6-4j, 40j], [13j, 30, 1-10j]]
    expect_2 = [[-5, -13j], [6+4j, 30], [-40j, 1+10j]]
    assert LA.conj_tpse(test_2) == expect_2
    return (test_1,), expect_1


def test_outer_product() -> Case:
    """Tests the function LA.outer_product()"""
    # Test for real vectors
    assert LA.outer_product(vector_a, vector_b) == \
            [[3, 6, 12], [1, 2, 4], [2, 4, 8]]
    # Test for real, complex
    assert LA.outer_product(vector_c, vector_d) == \
            [[-45+30j, 0, -27+18j], [-25j, 0, -15j], [40+5j, 0, 24+3j]]
    # Test for complex, real
    assert LA.outer_product(vector_d, vector_a) == \
            [[-9-6j, 5j, 8-1j], [-18-12j, 10j, 16-2j], [-36-24j, 20j, 32-4j]]
    return (vector_a, vector_b), [[3, 6, 12], [1, 2, 4], [2, 4, 8]]


# Run tests if file is run directly
if __name__ == '__main__':
    pytest.main(['test_LA.py'])
