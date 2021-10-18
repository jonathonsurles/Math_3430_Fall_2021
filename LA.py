"""Perform linear algebraic operations on matrices and vectors
"""


# Begin Homework 01-03 functions


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
    result: list[complex] = [element_a + element_b
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
    product_vector: list[complex] = [element * scalar for element in vector]

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
    product_matrix: list[list[complex]] = \
            [vector_scalar_multiply(vector, scalar) for vector in matrix]

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
    matrix_sum: list[list[complex]] = [add_vectors(column_a, column_b)
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
    product_vector: list[complex] = [0 for _ in matrix[0]]

    # Calculate the product of each column of matrix with the corresponding
    # element of vector, then add to the result vector
    for m_vector, v_element in zip(matrix, vector):
        inter_vector: list[complex] = \
                vector_scalar_multiply(m_vector, v_element)
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
    matrix_product: list[list[complex]] = \
            [matrix_vector_multiply(left_matrix, column)
            for column in right_matrix]

    # Return our resultant matrix
    return matrix_product


# End Homework 01-03 functions, begin Homework 04 functions


def cpx_conj(cpx: complex) -> float:
    """Conjugates a complex number

    Negate the imaginary portion of the input number, then return it

    Args:
        cpx: the complex number to be conjugated

    Returns:
        The complex conjugate of cpx
    """
    conj: complex = complex(cpx.real, -1 * cpx.imag)
    return conj


def abs_value(scalar: complex) -> float:
    """Finds the absolute value of a complex number

    Multiply scalar by its complex conjugate, then return the square root

    Args:
        scalar: a complex number

    Returns:
        The absolute value of the input scalar
    """
    # Calculate aboslute value, relying on (** .5) being positive root
    result: float = (scalar * cpx_conj(scalar)) ** .5

    # Since mathematically result.imag must be 0, return result.real for typing
    return result.real


def p_norm_finite(vector: list[complex], p: float=2) -> float:
    """Finds the p-norm of a vector. Defaults to 2-norm (euclidian norm)

    For every element in vector, add element^p to a running total. Then take
    the pth root of that sum, and return it

    Args:
        vector: a list of complex numbers, representing a vector
        p: a float. Must be real and >= 1.

    Returns:
        The p norm of vector
    """
    # Running total
    result: float = 0

    # Sum of each element to the pth power
    for element in vector:
        result += (abs_value(element) ** p)

    # pth root and return
    result **= (1 / p)
    return result


def inf_norm(vector: list[complex]) -> float:
    """Finds the infinite norm of a vector.

    Create a vector storing the absolute value for each element in vector.
    Find and return the greatest of those elements

    Args:
        vector: a list of complex numbers, representing a vector

    Returns:
        The infinite norm of vector, i.e. the greatest absolute value of all
        elements of vector.
    """
    result: float = None

    # Create a vector of absolute values
    abs_vector = [abs_value(element) for element in vector]

    # Find and return the greates absolute value
    result = max(abs_vector)
    return result


def p_norm(vector: list[complex], p: float=2, inf: bool=False) -> float:
    """Finds the p-norm of a vector. Defaults to 2-norm. Can calulate inf norm

    If inf is False, find the norm using the pre-existing p_norm_finite().
    If inf is True, find the norm using the pre-existing inf_norm()

    Args:
        vector: a list of complex numbers, representing a vector
        p: a float. Must be real and >= 1.
        inf: a boolean. If true, act as if p is infinite

    Returns:
        The p norm of vector, or infinity norm if inf is True
    """
    result: float = None

    # Finite case
    if not inf:
        result = p_norm_finite(vector, p)

    # Infinite case
    else:
        result = inf_norm(vector)

    return result


def inner_product(left_vector: list[complex],
                  right_vector: list[complex]) -> complex:
    """Finds the inner product of two vectors.

    Calculate the conjugate transpose of left_vector, them multiply
    element-wise this conjugate with right_vector, adding each term into the
    result. Return the result as a float if it is real, or as complex if needed

    Args:
        left_vector: a list of complex numbers, representing a vector.
        right_vector: a list of complex numbers, representing a vector. Must
                      be the same size as left_vector.

    Returns:
        The inner product <left_vector, right_vector>
    """
    # Calculate the conjugate transpose of left_vector
    left_vector_ct: list[complex] = [complex(element.real, -1 * element.imag)
            for element in left_vector]

    # Calculate the inner product
    result: complex = 0
    for left_element_c, right_element in zip(left_vector_ct, right_vector):
        result += left_element_c * right_element

    # Collapse real results to floats
    result = result.real if result.imag == 0 else result

    return result


# End Homework 04 Problems
