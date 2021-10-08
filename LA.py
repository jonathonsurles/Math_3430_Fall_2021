# TODO : unit testing for all functions


def add_vectors(vector_a: list[complex],
                vector_b: list[complex]) -> list[complex]:
    """Add two vectors stored as lists

    Builds the vector sum element-wise by adding each corresponding element
    of the two vectors

    Args:
        vector_a: A list of complex numbers representing a vector
        vector_b: A list of complex numbers representing a vector, must be the
                  same length as vector_a

    Returns:
        The sum of vector_a and vector_b, stored as a list of numbers
    """
    result = [element_a + element_b \
              for element_a, element_b in zip(vector_a, vector_b)]
    return result


def vector_scalar_multiply(vector: list[complex],
                           scalar: int) -> list[complex]:
    """Multiplies a vector times a scalar

    Builds the matrix-scalar product element-wise by multiplying each element
    of the vector by the scalar

    Args:
        vector: a list of complex numbers representing a vector
        scalar: a complex number

    Returns:
        The product of vector and scalar, represented as a list
    """
    # Create the product vector
    product_vector = [element * scalar for element in vector]

    # Return our product vector
    return product_vector


def matrix_scalar_multiply(matrix: list[list[complex]],
                           scalar: complex) -> list[list[complex]]:
    """Multiplies a matrix by a scalar

    Builds the matrix-scalar product vector-wise by multiplying each component
    vector of matrix by the scalar

    Args:
        matrix: a list of list of complex numbers, representing a matrix. Each
                component list represents a vector of the matrix, regardless
                of whether these vectors are rows or columns.
        scalar: a complex number

    Returns:
        The product of matrix times scalar, represented as a list of list of
        complex numbers, where each component list represents a vector of the
        same type as the input matrix (rows or columns)
    """

    # Create the product matrix
    product_matrix = [vector_scalar_multiply(vector, scalar) \
                      for vector in matrix]

    # Return our product matrix
    return product_matrix


def matrix_add(matrix_a: list[list[complex]],
               matrix_b: list[list[complex]]) -> list[list[complex]]:
    """Adds two matrices

    Builds the matrix sum by adding the corresponding columns of matrix_a and
    matrix_b

    Args:
        matrix_a: a list of list of complex numbers, representing a matrix.
                  Each component list representing either a row or column.
        matrix_b: a list of list of complex numbers, representing a matrix.
                  Each component list representing either a row or column.
                  The matrix must be of the same length as matrix_a, each
                  component list must be the same length as a component list
                  of matrix_a, and it must represent the same type of vector
                  as in matrix_a (row or column)

    Returns:
        The sum of matrix_a and matrix_b, represented as a list of list of
        complex numbers, where each component list represents either row
        vectors or column vectors, depending on the input matrices.
    """

    # Create the sum matrix
    matrix_sum = [add_vectors(column_a, column_b) \
                  for column_a, column_b in zip(matrix_a, matrix_b)]

    # Return our sum matrix
    return matrix_sum


def matrix_vector_multiply(matrix: list[list[complex]],
                           vector: list[complex]) -> list[complex]:
    """Multiplies a matrix by a vector

    Use the linear combination of columns method to multiply the input matrix
    by the input vector. Multiply each column of matrix by the corresponding
    element of vector, summing each of those vectors as calculated, then
    return that sum.

    Args:
        matrix: a list of list of complex numbers representing a matrix. Each
                component list must represent a column vector.
        vector: a list of complex numbers representing a column vector. Must
                have the same number of elements as matrix

    Returns:
        The matrix-vector product of matrix and vector, stored as a list of
        complex numbers.
    """

    # Initialize a resultant vector full of 0s
    product_vector = [0 for _ in matrix[0]]

    # Calculate the product of each column of matrix with the corresponding
    # element of vector, then add to the result vector
    for index in range(len(vector)):
        inter_vector = vector_scalar_multiply(matrix[index], vector[index])
        product_vector = add_vectors(product_vector, inter_vector)

    # Return our product vector
    return product_vector


def matrix_multiply(left_matrix: list[list[complex]],
                    right_matrix: list[list[complex]]) -> list[list[complex]]:
    """Multiplies two matrices together

    Performs the operation left_matrix * right_matrix by building a resultant
    matrix column by column, calculating each component using a linear
    combination of columns

    Args:
        left_matrix: A list of lists of complex numbers, representing a matrix.
                     Each component list must represent a column vector.
        right_matrix: A list of lists of complex numbers, representing a
                      matrix. Each component list must represent a column
                      vector, and the length of each column vector must be
                      equal to the number of vectors in left_matrix

    Returns:
        The product of left_matrix * right_matrix, stored as a list of lists
        of complex numbers, where each component list represents a column
        vector of the returned matrix.
    """

    # Create our resultant matrix
    matrix_product = [matrix_vector_multiply(left_matrix, column) \
                      for column in right_matrix]

    # Return our resultant matrix
    return matrix_product


# TODO: needs testing
def abs_value(scalar: complex) -> float:
    """Find the absolute value of a complex number
    
    Square the real and imaginary parts of scalar, then take the square root
    of their sum. Return that result

    Args:
        scalar: a complex number

    Returns:
        The absolute value of the input scalar
    """
    # Calculate aboslute value, relying on (** .5) being positive root
    result = ((scalar.real ** 2) + (scalar.imag ** 2)) ** .5

    # Return our result
    return result


# TODO: needs testing
def p_norm_finite(vector: list[complex], p=2: int) -> float:
    """Find the p-norm of a vector. Defaults to 2-norm (euclidian norm)

    For every element in vector, add element^p to a running total. Then take
    the pth root of that sum, and return it

    Args:
        vector: a list of complex numbers, representing a vector
        p: an integer (floats are also technically defined behavior). Must be
           real and >= 1

    Returns:
        The p norm of vector
    """
    # Running total
    result = 0.

    # Sum of each element to the pth power
    for element in vector:
        result += (abs_value(element) ** p)

    # pth root and return
    result ** (1 / p)
    return result


def inf_norm(vector: list[complex]) -> float:
    """Find the infinite norm of a vector.

    Create a vector storing the absolute value for each element in vector.
    Find and return the greatest of those elements

    Args:
        vector: a list of complex numbers, representing a vector

    Returns:
        The infinite norm of vector, i.e. the greatest absolute value of all
        elements of vector.
    """
    result = None

    # Create a vector of absolute values
    abs_vector = [abs_value(element) for element in vector]
    
    # Find and return the greates absolute value
    result = max(abs_vector)
    return result


# TODO: needs testing
def p_norm(vector: list[complex], p=2: int, inf=False: bool) -> float:
    """Find the p-norm of a vector. Defaults to 2-norm. Can calulate inf norm

    If inf is False, find the norm using the pre-existing p_norm_finite.
    If inf is True, create a vector storing the absolute value for each 
    element in vector. Find and return the greatest of those elements
    
    Args:
        vector: a list of complex numbers, representing a vector
        p: an integer (floats are also defined behacior). Must be real and
           >= 1.
        inf: a boolean. If true, act as if p is infinite

    Returns:
        The p norm of vector, or infinity norm if inf is True
    """
    result = None

    # Finite case
    if not inf:
        result = p_norm_finite(vector, p)

    # Infinite case
    else:
        result = inf_norm(vector)

    return result


# TODO: needs testing
def inner_product(left_vector: list[complex],
                  right_vector: list[complex]) -> complex:
    """Find the inner product of two vectors.

    Calculate the conjugate transpose of left_vector, them multiply
    element-wise this conjugate with right_vector, adding each term into the
    result. Return the result

    Args:
        left_vector: a list of complex numbers, representing a vector.
        right_vector: a list of complex numbers, representing a vector. Must
                      be the same size as left_vector.

    Returns:
        The inner product <left_vector, right_vector>
    """
    # Calculate the conjugate transpose of left_vector
    left_vector_ct = [complex(element.real, -1 * element.imag) \
                      for element in left_vector]

    # Calculate the inner product
    result = 0
    for left_element_c, right_element in zip(left_vector_ct, right_vector):
        result += left_element_c * right_element

    return result


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
