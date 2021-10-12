import LA


# Lambda to make dealing with complex numbers less ugly
c = lambda r, i : complex(r, i)


# Test variables for all functions
SCALAR_A = 4
SCALAR_B = 7
SCALAR_C = c(0, 1)
SCALAR_D = c(3, 4)
vector_a = [1, 2, 4]
vector_b = [3, 1, 2]
vector_c = [5, 0, 3]
vector_d = [c(-9, -6), c(0, 5), c(8, -1)]
matrix_a = [[1, 8, 4], [8, 7, 6], [3, 0, 9]]
matrix_b = [[5, 6, 2], [1, 7, 0], [4, 7, 7]]
matrix_c = [[5, 8, 6], [0, 5, 2], [9, 4, 3]]
matrix_d = [[c(-4, -7), c(6, -8), c(0, -5)],
            [c(2, 9), c(3, -4), c(6, 2)],
            [c(-5, 3), c(-1, 7), c(-1, 2)]]


def test_add_vectors():
    result_1 = [4, 3, 6]
    assert LA.add_vectors(vector_a, vector_b) == result_1
    result_2 = [c(-6, -6), c(1, 5), c(10, -1)]
    assert LA.add_vectors(vector_b, vector_d) == result_2


def test_vector_scalar_multiply():
    result_1 = [4, 8, 16]
    assert LA.vector_scalar_multiply(vector_a, SCALAR_A) == result_1
    result_2 = [c(6, -9), c(-5, 0), c(1, 8)]
    assert LA.vector_scalar_multiply(vector_d, SCALAR_C) == result_2


def test_matrix_scalar_multiply():
    result_1 = [[4, 32, 16], [32, 28, 24], [12, 0, 36]]
    assert LA.matrix_scalar_multiply(matrix_a, SCALAR_A) == result_1
    result_2 = [[c(7, -4), c(8, 6), c(5, 0)],
                [c(-9, 2), c(4, 3), c(-2, 6)],
                [c(-3, -5), c(-7, -1), c(-2, -1)]]
    assert LA.matrix_scalar_multiply(matrix_d, SCALAR_C) == result_2

def test_matrix_add():
    result_1 = [[6, 14, 6], [9, 14, 6], [7, 7, 16]]
    assert LA.matrix_add(matrix_a, matrix_b) == result_1
    result_2 = [[c(1, -7), c(12, -8), c(2, -5)],
                [c(3, 9), c(10, -4), c(6, 2)],
                [c(-1, 3), c(6, 7), c(6, 2)]]
    assert LA.matrix_add(matrix_b, matrix_d) == result_2

def test_matrix_vector_multiply():
    result_1 = [29, 22, 52]
    assert LA.matrix_vector_multiply(matrix_a, vector_a) == result_1
    result_2 = [24, 39, 20]
    assert LA.matrix_vector_multiply(matrix_b, vector_b) == result_2

def test_matrix_multiply():
    result_1 = [[59, 82, 74], [57, 57, 46], [81, 81, 121]]
    assert LA.matrix_multiply(matrix_a, matrix_b) == result_1
    result_2 = [[57, 128, 52], [13, 49, 14], [61, 103, 39]]
    assert LA.matrix_multiply(matrix_b, matrix_c) == result_2

def test_abs_value():
    assert LA.abs_value(-3.4) == 3.4
    assert LA.abs_value(0) == 0
    assert LA.abs_value(4) == 4
    assert LA.abs_value(c(3, 4)) == 5.0

def test_p_norm_finite():
    assert LA.p_norm_finite([3, 4]) == 5.0
    assert LA.p_norm_finite([5, c(3, 4)], p=1) == 10.0

def test_inf_norm():
    assert LA.inf_norm([3, 4]) == 4.0
    assert LA.inf_norm([3, c(3, 4)]) == 5.0

def test_p_norm():
    assert LA.p_norm([3, 4]) == 5.0
    assert LA.p_norm([5, c(3, 4)], p=1) == 10.0
    assert LA.p_norm([3, 4], inf=True) == 4.0
    assert LA.p_norm([3, c(3, 4)], inf=True) == 5.0

