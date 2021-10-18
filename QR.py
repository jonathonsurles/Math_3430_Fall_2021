"""Contains functions to perform QR factorization of matrices
"""


import LA


def gram_schmidt_unstable(matrix: list[list[complex]]) \
        -> list[list[list[complex]]]:
    """Performs the Gram-Schmidt method for reduced QR factorization

    DEPRECATED DO NOT USE
    For every column vector of the input matrix, store a copy of it. Then
    set this vector orthagonal to all initialized columns of q_matrix, storing
    each factor in r_matrix. Normalize this column vector, then repeat for all
    columns in the input matrix. Finally, return a list containing q_matrix and
    r_matrix.

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
    q_matrix = [[0 for m in matrix[0]] for n in matrix]
    # Create a 0 matrix that is square to the columns of matrix to represent R
    r_matrix = [[0 for m in matrix] for n in matrix]

    # Create Q and R
    for j in range(len(matrix)):
        vector = matrix[j] # Create a copy of the jth column of matrix
        for i in range(0, j): # For each already created column of Q...
            # Store the operations performed to orthagonalize the vector
            r_matrix[i][j] = LA.inner_product(matrix[i], matrix[j])
            # Orthagonalize vector relative to the current column
            vector = LA.add_vectors(vector, 
                    LA.vector_scalar_multiply(matrix[i], -1))
        # Normalize the now orthagonalized column and store that operation
        r_matrix[j][j] = LA.inner_product(vector, vector)
        q_matrix[j] = LA.vector_scalar_multiply(vector, 1 / r_matrix[j][j])
    
    # Return Q and R
    return [q_matrix, r_matrix]


# TODO: write paragraph summary
def gram_schmidt(matrix: list[list[complex]]) -> list[list[list[complex]]]:
    """Performs the Modified Gram-Schmidt method for reduced QR factorization

    ...

    Args:
        matrix: The matrix to be factored, represented as a list of list
                of column vectors

    Returns:
        A matrix representing Q in reduced QR factorization, represented
            as a list of lists, each component list being a column vector
        A matrix representing R in reduced QR factorization, represented
            as a list of lists, each component list being a column vector
    """
    ...
