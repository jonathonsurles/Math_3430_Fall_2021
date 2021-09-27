def add_vectors(vector_a: list[int], vector_b: list[int]) -> list[int]:
    """Add two vectors stored as lists

    Create an empty list of appropriate size and store the sums of the
    corresponding components of each input

    Args:
        vector_a: A list of integers representing a vector
        vector_b: A list of integers representing a vector, must be the same
                  length as vector_a

    Returns:
        The sum of vector_a and vector_b, stored as a list of numbers
    """
    result = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result


def vector_scalar_multiply(vector: list[int], scalar: int) -> list[int]:
    """Multiplies a vector times a scalar

    Create an empty list then store the result of vector times scalar by
    appending the scalar multiplied by each element of vector, in order

    Args:
        vector: a list of integers representing a vector
        scalar: an integer

    Returns:
        The product of vector and scalar, represented as a list
    """
    # Create a new list to server as our resultant vector
    product_vector = []

    # Compute the product by calculating each element then append it to result
    for element in vector:
        product_vector.append(element * scalar)

    # Return our product vector
    return product_vector


def matrix_scalar_multiply(matrix: list[list[int]], scalar: int) \
        -> list[list[int]]:
    """Multiplies a matrix by a scalar

    Creates an empty list, then appends each component vector of the input
    matrix multiplied by the scalar, in order

    Args:
        matrix: a list of list of integers, representing a matrix. Each
                component list represents a vector of the matrix, regardless
                of whether these vectors are rows or columns.
        scalar: an integer

    Returns:
        The product of matrix times scalar, represented as a list of list of
        integers, where each component list represents a vector of the same
        type as the input (rows or columns)
    """

    # Create a new list to serve as our resultant matrix
    product_matrix = []

    # Compute the product by calculating the product of each vector times the
    # scalar, and appending it to our result
    for vector in matrix:
        product_matrix.append(vector_scalar_multiply(vector, scalar))

    # Return our product matrix
    return product_matrix


def matrix_add(matrix_a: list[list[int]], matrix_b: list[list[int]]) \
        -> list[list[int]]:
    """Adds two matrices

    Creates an empty list, then appends the sum of eah corresponding vector
    of the input matrices

    Args:
        matrix_a: a list of list of integers, representing a matrix. Each
                  component list representing either a row or column vector.
        matrix_b: a list of list of integers, representing a matrix. Each
                  component list representing either a row or column vector.
                  The matrix must be of the same length as matrix_a, each
                  component list must be the same length as a component list
                  of matrix_a, and it must represent the same type of vector
                  as in matrix_a (row or column)

    Returns:
        The sum of matrix_a and matrix_b, represented as a list of list of
        integers, where each component list represents a vector, either row
        vectors or column vectors depending on the inputs.
    """

    # Create a new list to server as our resultant matrix
    matrix_sum = []

    # Compute the sum by calculating the sum of each pair of corresponding
    # vectors in matrix_a and matrix_b
    for index in range(len(matrix_a)):
        matrix_sum.append(add_vectors(matrix_a[index], matrix_b[index]))

    # Return our sum matrix
    return matrix_sum


def matrix_vector_multiply(matrix: list[list[int]], vector: list[int]) \
        -> list[int]:
    """Multiplies a matrix by a vector

    Use the linear combination of columns method to multiply the input matrix
    by the input vector. Multiply each column of matrix by the corresponding
    element of vector, then sum each of those vectors, returning that sum.

    Args:
        matrix: a list of list of integers representing a matrix. Each
                component list must represent a column vector.
        vector: a list of integers representing a column vector. Must have
                the same number of elements as matrix

    Returns:
        The matrix-vector product of matrix and vector, stored as a list of
        integers.
    """

    # Initialize a resultant vector full of 0s
    product_vector = []

    for element in matrix[0]:
        product_vector.append(0)

    # Initialize a list to store our intermediate vectors
    inter_vectors = []

    # Calculate the product of each column of matrix with the corresponding
    # element of vector, and store it as an intermediate vector
    for index in range(len(vector)):
        inter_vector = vector_scalar_multiply(matrix[index], vector[index])
        inter_vectors.append(inter_vector)

    # Calculate the final result by adding each intermediate vector
    for inter_vector in inter_vectors:
        product_vector = add_vectors(product_vector, inter_vector)

    # Return our product vector
    return product_vector


def matrix_multiply(left_matrix: list[list[int]],
                    right_matrix: list[list[int]]) -> list[list[int]]:
    """Multiplies two matrices together

    Performs the operation left_matrix * right_matrix by calculating each
    column using a linear combination fo columns, and appending each column
    together in a resultant matrix

    Args:
        left_matrix: A list of lists of integers, representing a matrix. Each
                     component list must represent a column vector.
        right_matrix: A list of lists of integers, representing a matrix. Each
                      component list must represent a column vector, and the
                      length of each column vector must be equal to the number
                      of vectors in left_matrix

    Returns:
        The product of left_matrix * right_matrix, stored as a list of lists
        of integers, where each component list represents a column vector.
    """

    # Define our resultant matrix
    matrix_product = []

    # Calculate each column using linear combination of columns and append to
    # the resultant matrix
    for column in right_matrix:
        matrix_product.append(matrix_vector_multiply(left_matrix, column))

    # Return our resultant matrix
    return matrix_product


# Test if file is run directly
if __name__ == '__main__':

    # Variables for testing
    scalar_a = 4
    scalar_b = 7
    vector_a = [1, 2, 4]
    vector_b = [3, 1, 2]
    vector_c = [5, 0, 3]
    matrix_a = [[1, 8, 4], [8, 7, 6], [3, 0, 9]]
    matrix_b = [[5, 6, 2], [1, 7, 0], [4, 7, 7]]
    matrix_c = [[5, 8, 6], [0, 5, 2], [9, 4, 3]]

    """
    Test Cases
    These could have been rolled into a testing function but I was unsure
    if that would be allowed. They all follow the general format:
    test = func(in1, in2)
    expected = {expected}
    result = test == expected
    print(pass if result, else fail)
    if not result:
        print(expected, test)
    """

    # add_vectors(vector_a, vector_b) should output [4, 3, 6]
    a_v_t1 = add_vectors(vector_a, vector_b)
    a_v_e1 = [4, 3, 6]
    a_v_r1 = a_v_t1 == a_v_e1
    print(f'add_vectors test #1: {"pass" if a_v_r1 else "fail"}')
    if not a_v_r1:
        print(f'Expected result: {a_v_e1} | Actual: {a_v_t1}')

    # add_vectors(vector_a, vector_c) should output [6, 2, 7]
    a_v_t2 = add_vectors(vector_a, vector_c)
    a_v_e2 = [6, 2, 7]
    a_v_r2 = a_v_t2 == a_v_e2
    print(f'add_vectors test #2: {"pass" if a_v_r2 else "fail"}')
    if not a_v_r2:
        print(f'Expected result: {a_v_e2} | Actual: {a_v_t2}')

    # vector_scalar_multiply(vector_a, scalar_a) should output [4, 8, 16]
    v_s_m_t1 = vector_scalar_multiply(vector_a, scalar_a)
    v_s_m_e1 = [4, 8, 16]
    v_s_m_r1 = v_s_m_t1 == v_s_m_e1
    print(f'vector_scalar_multiply test #1: {"pass" if v_s_m_r1 else "fail"}')
    if not v_s_m_r1:
        print(f'Expected result: {v_s_m_e1} | Actual: {v_s_m_t1}')

    # vector_scalar_multiply(vector_b, scalar_b) should output [21, 7, 14]
    v_s_m_t2 = vector_scalar_multiply(vector_b, scalar_b)
    v_s_m_e2 = [21, 7, 14]
    v_s_m_r2 = v_s_m_t2 == v_s_m_e2
    print(f'vector_scalar_multiply test #2: {"pass" if v_s_m_r2 else "fail"}')
    if not v_s_m_r2:
        print(f'Expected result: {v_s_m_e2} | Actual: {v_s_m_t2}')

    # matrix_scalar_multiply(matrix_a, scalar_a) should output:
    # [[4, 32, 16], [32, 28, 24], [12, 0, 36]]
    m_s_m_t1 = matrix_scalar_multiply(matrix_a, scalar_a)
    m_s_m_e1 = [[4, 32, 16], [32, 28, 24], [12, 0, 36]]
    m_s_m_r1 = m_s_m_t1 == m_s_m_e1
    print(f'matrix_scalar_multiply test #1: {"pass" if m_s_m_r1 else "fail"}')
    if not m_s_m_r1:
        print(f'Expected result: {m_s_m_e1} | Actual: {m_s_m_t1}')

    # matrix_scalar_multiply(matrix_b, scalar_b) should output:
    # [[35, 42, 14], [7, 49, 0], [28, 49, 49]]
    m_s_m_t2 = matrix_scalar_multiply(matrix_b, scalar_b)
    m_s_m_e2 = [[35, 42, 14], [7, 49, 0], [28, 49, 49]]
    m_s_m_r2 = m_s_m_t2 == m_s_m_e2
    print(f'matrix_scalar_multiply test #2: {"pass" if m_s_m_r2 else "fail"}')
    if not m_s_m_r2:
        print(f'Expected result: {m_s_m_e2} | Actual: {m_s_m_t2}')

    # matrix_add(matrix_a, matrix_b) should output:
    # [[6, 14, 6], [9, 14, 6], [7, 7, 16]]
    m_a_t1 = matrix_add(matrix_a, matrix_b)
    m_a_e1 = [[6, 14, 6], [9, 14, 6], [7, 7, 16]]
    m_a_r1 = m_a_t1 == m_a_e1
    print(f'matrix_add test #1: {"pass" if m_a_r1 else "fail"}')
    if not m_a_r1:
        print(f'Expected result: {m_a_e1} | Actual: {m_a_t1}')

    # matrix_add(matrix_b, matrix_c) should output:
    # [[10, 14, 8], [1, 12, 2], [13, 11, 10]]
    m_a_t2 = matrix_add(matrix_b, matrix_c)
    m_a_e2 = [[10, 14, 8], [1, 12, 2], [13, 11, 10]]
    m_a_r2 = m_a_t2 == m_a_e2
    print(f'matrix_add test #2: {"pass" if m_a_r2 else "fail"}')
    if not m_a_r2:
        print(f'Expected result: {m_a_e2} | Actual: {m_a_t2}')

    # matrix_vector_multiply(matrix_a, vector_a) should output [29, 22, 52]
    m_v_m_t1 = matrix_vector_multiply(matrix_a, vector_a)
    m_v_m_e1 = [29, 22, 52]
    m_v_m_r1 = m_v_m_t1 == m_v_m_e1
    print(f'matrix_vector_multiply test #1: {"pass" if m_v_m_r1 else "fail"}')
    if not m_v_m_r1:
        print(f'Expected result: {m_v_m_e1} | Actual: {m_v_m_t1}')

    # matrix_vector_multiply(matrix_b, vector_b) should output [24, 39, 20]
    m_v_m_t2 = matrix_vector_multiply(matrix_b, vector_b)
    m_v_m_e2 = [24, 39, 20]
    m_v_m_r2 = m_v_m_t2 == m_v_m_e2
    print(f'matrix_vector_multiply test #2: {"pass" if m_v_m_r2 else "fail"}')
    if not m_v_m_r2:
        print(f'Expected result: {m_v_m_e2} | Actual: {m_v_m_t2}')

    # matrix_multiply(matrix_a, matrix_b) should output:
    # [[59, 82, 74], [57, 57, 46], [81, 81, 121]]
    m_m_t1 = matrix_multiply(matrix_a, matrix_b)
    m_m_e1 = [[59, 82, 74], [57, 57, 46], [81, 81, 121]]
    m_m_r1 = m_m_t1 == m_m_e1
    print(f'matrix_multiply test #1: {"pass" if m_m_r1 else "fail"}')
    if not m_m_r1:
        print(f'Expected result: {m_m_e1} | Actual: {m_m_t1}')

    # matrix_multiply(matrix_b, matrix_c) should output:
    # [[57, 128, 52], [13, 49, 14], [61, 103, 39]]
    m_m_t2 = matrix_multiply(matrix_b, matrix_c)
    m_m_e2 = [[57, 128, 52], [13, 49, 14], [61, 103, 39]]
    m_m_r2 = m_m_t2 == m_m_e2
    print(f'matrix_multiply test #2: {"pass" if m_m_r2 else "fail"}')
    if not m_m_r2:
        print(f'Expected result: {m_m_e2} | Actual: {m_m_t2}')
