"""Contains functions to perform QR factorization of matrices"""


import LA


# Type aliases
Vector = list[complex]
Matrix = list[list[complex]]


def normalize(vector: Vector) -> list[Vector, float]:
    """Normalizes a vector

    Calculate the norm of the input vector. Then, multiply the vector by the
    reciprocal of norm. Return the vector and the norm as a list

    Args:
        vector: the vector to be normalized

    Returns:
        A list, where the first element is the normalized vector and the
        second element is the norm of the original vector
    """
    norm: float = LA.p_norm(vector)
    result: Vector = LA.vector_scalar_multiply(vector, 1 / norm)

    return [result, norm]


def orthagonalize(vector: Vector, basis: Vector) -> list[Vector, complex]:
    """Calculates the vector rejection of vector on basis

    Calculate the inner product between vector and basis and store it. Use that
    inner product to calculate the negated vector projection of vector on
    basis, then subtract that from vector. Return that vector rejection and the
    inner product used to calculate it.

    Args:
        vector: the vector to be orthagonalized
        basis: the vector to be orthagonalized against. Must be normalized.

    Returns:
        A list, where the first element is the orthagonalized vector, and the
        second element is the inner product of the vectors used to calculate it
    """
    factor: complex = LA.inner_product(vector, basis)
    neg_proj: Vector = LA.vector_scalar_multiply(basis, -1 * factor)
    result: Vector = LA.add_vectors(vector, neg_proj)

    return [result, factor]


def gram_schmidt(matrix: Matrix) -> list[Matrix, Matrix]:
    """Performs the Modified Gram-Schmidt method for reduced QR factorization

    First, initialize q_matrix (Q) to be a copy of the input matrix. and
    r_matrix (R) to be a zero matrix of the appropriate size. Then, iterate
    over every column vector in Q. First, normalize the vector and store the
    normalization in R. Then, orthagonalize every following vector in Q
    relative to the current working column, storing this orthagonalization
    in R. Finally, return Q and R as a list.

    Args:
        matrix: The matrix to be factored, represented as a list of list
          of column vectors

    Returns:
        A list of matrices, each represented as a list of lists, each component
        list representing a column vector. The first matrix is the orthonormal
        matrix Q and the second matrix is the upper triangular matrix R
    """
    # Let q_matrix (Q) be a copy of matrix, and r_matrix (R) be a 0 matrix
    q_matrix: Matrix = [column[:] for column in matrix]
    r_matrix: Matrix = [[0 for m in matrix] for n in matrix]

    # Orthonormalize Q and store the processes in R
    for i, vector in enumerate(q_matrix):
        # Perform a normalization operation on the working column and store
        norm_operation = normalize(vector)
        q_matrix[i] = norm_operation[0]
        r_matrix[i][i] = norm_operation[1]
        # Orthagonalize the following vectors in Q relative to working column
        for j, orth_vector in enumerate(q_matrix[i+1:], start=i+1):
            # Perform an orthagonalization operation on Q_j and store factor
            orth_operation = orthagonalize(orth_vector, vector)
            q_matrix[j] = orth_operation[0]
            r_matrix[j][i] = orth_operation[1]

    # Return Q and R as a list
    return [q_matrix, r_matrix]


def orthonormalize(matrix: Matrix) -> Matrix:
    """Returns an orthonormal matrix with the same span as the input matrix

    Performs modified gram-schmidt method for QR factorization and returns Q

    Args:
        matrix: The matrix to be orthonormalized, represented as a list of
          lists, where each component list represents a column vector

    Returns:
        An orthonormal matrix with the same span as the input matrix
    """
    # Might be kinda cheating but hey it works
    return gram_schmidt(matrix)[0]


def _householder_q_k(matrix_r: Matrix, k: int) -> Matrix:
    """Calculates q_k from the kth column of a matrix R for Householder QR

    Performs the mathematical algorthm to calculate q_k for Householder QR
    factorization.

    Args:
        matrix_r: (R), the original matrix from which q_k should be generated
        k: which column should be used as the base to generate q_k

    Returns:
        A matrix q_k such that q_k * matrix_r sets the kth column of matrix_r
        to be upper triangular (below the kth element are only zeroes)
    """
    # Let d_m (m) be the number of rows of matrix_r
    d_m = len(matrix_r[0])

    # Let q_k = the mxm identity matrix to start
    q_k: Matrix
    q_k = [[1 if i==j else 0 for i in range(d_m)] for j in range(d_m)]

    # Calculate v
    vec_x: Vector = matrix_r[k][k:]
    vec_v: Vector = q_k[k][k:]
    v_scl: float = LA.p_norm(vec_x) * (1 if vec_x[0].real >= 0 else -1)
    vec_v = LA.vector_scalar_multiply(vec_v, v_scl)
    vec_v = LA.add_vectors(vec_v, vec_x)

    # Use v to calculate F-I
    mat_f: Matrix = LA.outer_product(vec_v, vec_v)
    f_scl: float = -2 / LA.inner_product(vec_v, vec_v)
    mat_f = LA.matrix_scalar_multiply(mat_f, f_scl)

    # q_k is currently I, so adding F-I to the bottom right corner sets the
    # bottom corner to (F-I)+I = F
    for i, f_col in enumerate(mat_f, start=k):
        q_k[i] = LA.add_vectors(q_k[i][:k] + f_col, q_k[i])

    return q_k


def householder_orth(matrix: Matrix) -> list[Matrix, Matrix]:
    """Performs the householder orthagonalization method for QR factorization

    Initialize matrix_q (Q) as an identity matrix with the same number of rows
    as the input matrix, and matrix_r (R) as a copy of the input matrix. Then
    find successive matrices Q_k such that Q_k * R sets the kth column of R
    to be upper triangular. Update Q and R such that they are multiplied by
    Q_k, then once R is upper triangular, take the conjugate transpose of Q,
    then finally return the list [Q, R]

    Args:
        matrix: The matrix to be factored, represented as a list of lists of
          complex numbers

    Returns:
        A list of matrices, where the first element is the orthogonal matrix
        Q and the second element is the upper triangular matrix R
    """
    # Dimensions of the input matrix for calculations
    d_m: int = len(matrix[0])  # m = number of rows
    d_n: int = len(matrix)  # n = number of columns

    # If matrix is mxn, let matrix_q (currently Q*) = the mxm identity
    matrix_q: Matrix
    matrix_q = [[1 if i==j else 0 for i in range(d_m)] for j in range(d_m)]
    # Let matrix_r (R) start as a copy of the input matrix
    matrix_r: Matrix = [column[:] for column in matrix]

    for k, _ in enumerate(matrix_r):
        # Find Q_k
        mat_q_k = _householder_q_k(matrix_r, k)
        # Use Q_k to continue our computation of Q* and R
        matrix_r = LA.matrix_multiply(mat_q_k, matrix_r)
        matrix_q = LA.matrix_multiply(mat_q_k, matrix_q)

    # Calculate Q given Q*: calculate Q**
    matrix_q = LA.conj_tpse(matrix_q)

    return [matrix_q, matrix_r]
