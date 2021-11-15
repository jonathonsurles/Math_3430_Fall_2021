"""Contains functions to find the least squares solutions of equations."""


import LA
import QR


# Type aliases
Vector = list[complex]
Matrix = list[list[complex]]


def least_squares(matrix: Matrix, vector: Vector) -> Vector:
    """Finds the least squares solution of a matrix-vector product, Ax = b

    ...

    Args:
        matrix: The matrix A in an equation Ax = b
        vector: The vector b in an equation Ax = b

    Returns:
        The vector x in an equation Ax = b
    """
    # Result vector, initialized with None to spot errors
    vec_x: Vector = [None for _ in matrix]
    # Calculate Q, R
    mat_q: Matrix
    mat_r: Matrix
    mat_q, mat_r = QR.householder(matrix)
    # Calculate v = Q*b
    vec_v: Vector = LA.matrix_vector_multiply(LA.conj_tpse(mat_q), vector)

    # Perform back substitution
    # Iterates x_el from (len(vec_x) - 1) to 0
    for x_el in range(len(matrix) - 1, 0 - 1, -1):
        # Find the contributions of known elements of x
        cont: complex = 0
        for i in range(x_el, len(vec_x)):
            if i != x_el:
                cont += vec_x[i] * mat_r[i][x_el]
        # Use the contribution and the vector v to find the element of x
        vec_x[x_el] = (vec_v[x_el] - cont) / mat_r[x_el][x_el]

    return vec_x
