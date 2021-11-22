"""Perform linear algebraic operations on matrices and vectors"""


# Type Aliases
Vector = list[complex]
Matrix = list[list[complex]]


def add_vectors(vector_a: Vector, vector_b: Vector) -> Vector:
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
    # Create the sum vector
    result: Vector = [element_a + element_b
            for element_a, element_b in zip(vector_a, vector_b)]

    return result


def vector_scalar_multiply(vector: Vector, scalar: complex) -> Vector:
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
    product_vector: Vector = [element * scalar for element in vector]

    return product_vector


def matrix_scalar_multiply(matrix: Matrix, scalar: complex) -> Matrix:
    """Multiplies a matrix by a scalar

    Builds the matrix-scalar product vector-wise by multiplying each component
    vector of matrix by the scalar

    Args:
        matrix: a list of list of complex numbers, representing a matrix. Each
          component list represents a vector of the matrix, regardless of
          whether these vectors are rows or columns.
        scalar: a complex number

    Returns:
        The product of matrix times scalar, represented as a list of list of
        complex numbers, where each component list represents a vector of the
        same type as the input matrix (rows or columns)
    """

    # Create the product matrix
    product_matrix: Matrix = \
            [vector_scalar_multiply(vector, scalar) for vector in matrix]

    return product_matrix


def matrix_add(matrix_a: Matrix, matrix_b: Matrix) -> Matrix:
    """Adds two matrices

    Builds the matrix sum by adding the corresponding columns of matrix_a and
    matrix_b

    Args:
        matrix_a: a list of list of complex numbers, representing a matrix.
          Each component list representing either a row or column.
        matrix_b: a list of list of complex numbers, representing a matrix.
          Each component list representing either a row or column. The matrix
          must have the same dimensions as matrix_a, and each component list
          must represent the same type of vector as in matrix_a (row or column)

    Returns:
        The sum of matrix_a and matrix_b, represented as a list of list of
        complex numbers, where each component list represents either row
        vectors or column vectors, depending on the input matrices.
    """

    # Create the sum matrix
    matrix_sum: Matrix = [add_vectors(column_a, column_b)
            for column_a, column_b in zip(matrix_a, matrix_b)]

    return matrix_sum


def matrix_vector_multiply(matrix: Matrix, vector: Vector) -> Vector:
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
    product_vector: Vector = [0 for _ in matrix[0]]

    # Calculate the product of each column of matrix with the corresponding
    # element of vector, then add to the result vector
    for column, v_element in zip(matrix, vector):
        inter_vector: Vector = vector_scalar_multiply(column, v_element)
        product_vector = add_vectors(product_vector, inter_vector)

    return product_vector


def matrix_multiply(left_matrix: Matrix, right_matrix: Matrix) -> Matrix:
    """Multiplies two matrices together

    Performs the operation left_matrix * right_matrix by building a resultant
    matrix column by column, calculating each component using a linear
    combination of columns

    Args:
        left_matrix: A list of lists of complex numbers, representing a matrix.
          Each component list must represent a column vector.
        right_matrix: A list of lists of complex numbers, representing a
          matrix. Each component list must represent a column vector, and the
          length of each must be equal to the length of left_matrix

    Returns:
        The product of left_matrix * right_matrix, stored as a list of lists
        of complex numbers, where each component list represents a column
        vector of the returned matrix.
    """

    # Create our resultant matrix
    matrix_product: Matrix = [matrix_vector_multiply(left_matrix, column)
            for column in right_matrix]

    return matrix_product


def abs_value(scalar: complex) -> float:
    """Finds the absolute value of a complex number

    Multiply scalar by its complex conjugate, then return the square root

    Args:
        scalar: a complex number

    Returns:
        The absolute value of the input scalar
    """
    # Calculate aboslute value using complex conjugate. Mathematically, the
    # imaginary component must be 0, so throw it away using .real
    result: float = ((scalar * scalar.conjugate()) ** .5).real

    return result


def p_norm_finite(vector: Vector, p: float=2) -> float:
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

    # Sum each element to the pth power
    for element in vector:
        result += (abs_value(element) ** p)

    # pth root and return
    result **= (1 / p)
    return result


def inf_norm(vector: Vector) -> float:
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
    abs_vector: Vector = [abs_value(element) for element in vector]

    # Find and return the greatest absolute value
    result = max(abs_vector)
    return result


def p_norm(vector: Vector, p: float=2, inf: bool=False) -> float:
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


def p_q_norm(matrix: Matrix, p: float=2, q: float=1) -> float:
    """Finds the p,q norm of a vector for finite p, q. Defaults to 2,1 norm.

    Find the p-norm of each input vector, and put those norms as a vector.
    Then calculate the q-norm of the vector of norms and return it.

    Args:
        matrix: A matrix as a list of lists of complex numbers
        p: the norm to take of the component vectors
        q: the norm to take of the vector norms

    Returns:
        The p,q norm of the input matrix
    """
    norms: Vector = [p_norm(vec, p=p) for vec in matrix]
    return p_norm(norms, p=q)


def inner_product(left_vector: Vector, right_vector: Vector) -> complex:
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
    # Calculate the conjugate "transpose" of left_vector
    left_vector_ct: Vector = [element.conjugate() for element in left_vector]

    # Calculate the inner product
    result: complex = 0
    for left_element_c, right_element in zip(left_vector_ct, right_vector):
        result += left_element_c * right_element

    # Collapse real results to floats
    result = result.real if result.imag == 0 else result

    return result


def conj_tpse(matrix: Matrix) -> Matrix:
    """Finds the conjugate transpose of a matrix

    Creates a matrix that is the conjugate transpose of the input matrix then
    returns it.

    Args:
        matrix: A matrix, represented as a list of lists of complex numbers.

    Returns:
        The conjugate transpose of the matrix, represented in the same way.
    """
    # Get the dimensions
    d_m: int = len(matrix[0])  # m = number of rows in input
    d_n: int = len(matrix)  # n = number of columns in input
    # Calculate the conjutgate transpose
    result: Matrix = [[matrix[row][col].conjugate()
            for row in range(d_n)] for col in range(d_m)]
    return result


def outer_product(left_vector: Vector, right_vector: Vector) -> Matrix:
    """Finds the outer product of two column vectors

    Calculate the conjugate transpose of right_vector and transform each
    vector into a matrix representation. Multiply these vector-matrices using
    the matrix multiply function, then return that matrix.

    Args:
        left_vector: a list of complex numbers, representing a column vector.
        right_vector: a list of complex numbers, representing a column vector.

    Returns:
        The outer product matrix = left_vector right_vector*
    """
    # Calculate the conjugate transpose of right_vector as a matrix
    right_vector_ct: Matrix = conj_tpse([right_vector])
    # Set the left vector to its matrix representation
    left_vector_m: Matrix = [left_vector]
    # Perform the outer product
    result = matrix_multiply(left_vector_m, right_vector_ct)
    return result


# Lambdas for margin of error comparison
vector_margin = lambda v1, v2 : p_norm(add_vectors(
        vector_scalar_multiply(v1, -1), v2))
vector_margin.__doc__ = \
        'Finds the 2-norm of the difference between two vectors\n'
matrix_margin = lambda m1, m2 : p_q_norm(matrix_add(
        matrix_scalar_multiply(m1, -1), m2))
matrix_margin.__doc__ = \
        'Finds the 2,1-norm of the difference between two matrices\n'
