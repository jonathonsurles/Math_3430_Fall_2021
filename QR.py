"""Contains functions to perform QR factorization of matrices
"""


import LA


def gram_schmidt_unstable(matrix: list[list[complex]]) \
        -> list[list[list[complex]]]:
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
    for j in range(len(matrix)):
        vector = matrix[j] # Create a copy of the jth column of matrix
        for i in range(0, j): # For each already created column of Q...
            # Store the operation we need to orthagonalize the vector to Q_i
            r_matrix[j][i] = LA.inner_product(matrix[i], matrix[j])
            # Orthagonalize vector relative to the current column
            vector = LA.add_vectors(vector, 
                     LA.vector_scalar_multiply(matrix[i], -1 * r_matrix[j][i]))
        # Normalize the now orthagonalized column and store that operation
        r_matrix[j][j] = LA.p_norm(vector)
        q_matrix[j] = LA.vector_scalar_multiply(vector, 1 / r_matrix[j][j])
    
    # Return Q and R
    return [q_matrix, r_matrix]


def gram_schmidt(matrix: list[list[complex]]) -> list[list[list[complex]]]:
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
    q_matrix = [[x for x in column] for column in matrix]
    r_matrix = [[0 for m in matrix] for n in matrix]

    # Orthonormalize Q and store the processes in R
    for i in range(len(q_matrix)):
        # Store the norm of the working column vector and then normalize
        r_matrix[i][i] = LA.p_norm(q_matrix[i])
        q_matrix[i] = LA.vector_scalar_multiply(
                      q_matrix[i], 1 / r_matrix[i][i])
        # Orthagonalize the following vectors in Q relative to working column
        for j in range(i+1, len(q_matrix)):
            # Store the orthagonalization factor in R, then orthagonalize Q_j
            r_matrix[j][i] = LA.inner_product(q_matrix[i], q_matrix[j])
            q_matrix[j] = LA.add_vectors(q_matrix[j],
                  vector_scalar_multiply(q_matrix[i], -1 * r_matrix[j][i]))

    # Return Q and R as a list
    return [q_matrix, r_matrix]
