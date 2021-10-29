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
    result: list[complex] = LA.vector_scalar_multiply(vector, 1 / norm)

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
    neg_proj: list[complex] = LA.vector_scalar_multiply(basis, -1 * factor)
    result: list[complex] = LA.add_vectors(vector, neg_proj)

    return [result, factor]


def gram_schmidt_unstable(matrix: Matrix) -> list[Matrix, Matrix]:
    """Performs the Gram-Schmidt method for reduced QR factorization

    DEPRECATED DO NOT USE
    First, create q_matrix (Q) and r_matrix (R) to be 0 matrices of the
    appropriate size. Then to calculate Q and R, iterate over every column
    vector of the input matrix. First, we will store a copy of it. Then we will
    set this vector orthagonal to all initialized columns of q_matrix, storing
    each factor in r_matrix. Normalize this column vector, then repeat for all
    columns in the input matrix. Finally, once iteration is complete, return a
    list containing q_matrix and r_matrix.

    Args:
        matrix: The matrix to be factored, represented as a list of list
                of column vectors

    Returns:
        A matrix representing Q in reduced QR factorization, represented
            as a list of lists, each component list being a column vector
        A matrix representing R in reduced QR factorization, represented
            as a list of lists, each component list being a column vector
    """
    # Create a 0 matrix of the same size as matrix to represent Q
    q_matrix = [[0 for _ in column] for column in matrix]
    # Create a 0 matrix that is square to the columns of matrix to represent R
    r_matrix = [[0 for m in matrix] for n in matrix]

    # Create Q and R
    for j, _ in enumerate(matrix):
        vector = matrix[j][:] # Create a copy of the jth column of matrix
        for i in range(0, j): # For each already created column of Q...
            # Orthagonalize vector to the working column and store the operation
            orth_operation = orthagonalize(vector, matrix[i])
            vector = orth_operation[0]
            r_matrix[j][i] = orth_operation[1]
        # Normalize the now orthagonalized column and store that operation
        norm_operation = normalize(vector)
        q_matrix[j] = norm_operation[0]
        r_matrix[j][j] = norm_operation[1]

    # Return Q and R
    return [q_matrix, r_matrix]


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
        A matrix representing Q in reduced QR factorization, represented
            as a list of lists, each component list being a column vector
        A matrix representing R in reduced QR factorization, represented
            as a list of lists, each component list being a column vector
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


def householder_orth(matrix: Matrix) -> list[Matrix, Matrix]:
    """Performs the householder orthagonalization method for QR factorization

    TODO: Long explanation

    Args:
        matrix: The matrix to be factored, represented as a list of lists of
                complex numbers.

    Returns:
        A list of matrices, where the first element is the orthonormal matrix
        Q and the second element is the upper triangular matrix R
    """
    # TODO: breakout functions?
    # 1. build identity
    # 2. build Q_k
    # 3. build F
    # 4. build v
    # 5. matrix conjugate transpose

    # If matrix is mxn, let matrix_q_ct (Q*) = the mxm identity
    matrix_q_ct: Matrix = [[1 if i==j else 0 for i, _ in enumerate(matrix[0])] for j, _ in enumerate(matrix[0])]
    # Let matrix_r (R) start as a copy of the input matrix
    matrix_r: Matrix = [column[:] for column in matrix]

    for k, column in enumerate(matrix_r):
        # Find Q_k
        # Let Q_k = the mxm identity matrix
        q_k: Matrix = [[1 if i==j else 0 for i, _ in enumerate(matrix[0])] for j, _ in enumerate(matrix[0])]
        # Set the top left to the appropriate sized identity
        for i in range(k):
            q_k[i][i] = 1

        # Calculate v
        vec_x: Vector = matrix_r[k][k:]
        vec_v: Vector = q_k[k][k:]
        v_scale: float = LA.p_norm(vec_x) * (1 if vec_x[0] >= 0 else -1)
        vec_v = LA.vector_scalar_multiply(vec_v, v_scale)
        vec_v = LA.add_vectors(vec_v, vec_x)

        # Use v to calculate F
        mat_i: Matrix = [[1 if i==j else 0 for i, _ in enumerate(matrix[0])] for j, _ in enumerate(matrix[0])]
        mat_f: Matrix = LA.outer_product(vec_v, vec_v)
        f_scale: float = -2 / LA.inner_product(vec_v, vec_v)
        mat_f = LA.matrix_scalar_multiply(mat_f, f_scale)
        mat_f = LA.matrix_add(mat_f, mat_i)

        # Set the latter portion of q_k equal to F
        # List slicing nonsense that I will certainly forget how it works
        for i, f_col in enumerate(mat_f, start=k):
            q_k[i] = q_k[i][:k] + f_col
    
        # Use our finally complete Q_k to continue our computation of Q* and R
        matrix_r = LA.matrix_multiply(q_k, matrix_r)
        matrix_q_ct = LA.matrix_multiply(q_k, matrix_q_ct)

    # Calculate Q given Q*
    matrix_q: Matrix = [[matrix_q_ct[i][j].conjugate() for i, _ in enumerate(matrix_q_ct[0])] for j, _ in enumerate(matrix_q_ct)]

    return [matrix_q, matrix_r]
