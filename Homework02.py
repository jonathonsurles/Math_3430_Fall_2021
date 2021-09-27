"""
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python
functions.

For Problems #0-5 from HW01, Do the following.



1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment.

3) Test each of your functions on at least 2 inputs.

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version
to github after that date.
"""


# Example:

# Problem 00

"""
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b.

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b.

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""


def add_vectors(vector_a, vector_b):
    result = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result


# End Example


# Problem 01
'''
Write an algorithm to implement scalar-vector multiplication.

Q1: What do we have?
A1: A vector "vector" stored as a list and a scalar "scalar" stored as an
    integer

Q2: What do we want?
A2: The product of vector and scalar stored as a list

Q3: How will we get there?
A3: Create an empty list and then store vector times scalar by appending, in
    order, the scalar multiplied by each element of vector

def vector_scalar_multiply(vector, scalar):

  # Create a new list to server as our resultant vector
  product_vector = []

  # Compute the product by calculating each element then append it to result
  for element in vector:
    append (element * scalar) to product_vector

  # Return our product vector
  return product_vector
'''


def vector_scalar_multiply(vector, scalar):
    # Create a new list to server as our resultant vector
    product_vector = []

    # Compute the product by calculating each element then append it to result
    for element in vector:
        product_vector.append(element * scalar)

    # Return our product vector
    return product_vector


# Problem 02
'''
Write an algorithm to implement scalar-matrix multiplication.

Q1: What do we have?
A1: A matrix "matrix" stored as a 2D list where each component list represents
    a column vector, and a scalar "scalar" stored as an integer

Q2: What do we want?
A2: The product of matrix and scalar stored as a 2D list where each component
    lists represents a column vector

Q3: How will we get there?
A3: Create an empty list then append in order each component vector of matrix
    multiplied by the scalar

def matrix_scalar_multiply(matrix, scalar):

  # Create a new list to serve as our resultant matrix
  product_matrix = []

  # Compute the product by calculating the product of each vector times the
  # scalar, and appending it to our result
  for vector in matrix:
    append vector_scalar_multiply(vector, scalar) to product_matrix

  # Return our product matrix
  return product_matrix
'''


def matrix_scalar_multiply(matrix, scalar):

    # Create a new list to serve as our resultant matrix
    product_matrix = []

    # Compute the product by calculating the product of each vector times the
    # scalar, and appending it to our result
    for vector in matrix:
        product_matrix.append(vector_scalar_multiply(vector, scalar))

    # Return our product matrix
    return product_matrix


# Problem 03
'''
Write an algorithm to implement matrix addition.

Q1: What do we have?
A1: Two matrices "matrix_a" and "matrix_b", stored as a 2D list, where each
    component list represents a column vector. Assumed to be the same size.

Q2: What do we want?
A2: The sum of matrix_a and matrix_b, stored as a 2D list, where each
    component list represents a column vector.

Q3: How will we get there?
A3: Create an empty list then append in order the sum of each corresponding
    component vector of matrix_a and matrix_b

def matrix_add(matrix_a, matrix_b):

  # Create a new list to server as our resultant matrix
  matrix_sum = []

  # Compute the sum by calculating the sum of each pair of corresponding
  # vectors in matrix_a and matrix_b
  for index in range(length(matrix_a)):
    append add_vectors(matrix_a[index], matrix_b[index]) to matrix_sum

  # Return our sum matrix
  return matrix_sum
'''


def matrix_add(matrix_a, matrix_b):

    # Create a new list to server as our resultant matrix
    matrix_sum = []

    # Compute the sum by calculating the sum of each pair of corresponding
    # vectors in matrix_a and matrix_b
    for index in range(len(matrix_a)):
        matrix_sum.append(add_vectors(matrix_a[index], matrix_b[index]))

    # Return our sum matrix
    return matrix_sum


# Problem 04
'''
Write an algorithm to implement matrix-vector multiplication using the linear
combination of columns method. You must use the algorithms from Problem #0 and
Problem #1.

Q1: What do we have?
A1: A matrix "matrix" stored as a 2D list, where each component list
    represents a column vector, and a column vector "vector", store as a list.
    Assumed to be compatible to multiply.

Q2: What do we want?
A2: The matrix-vector product of matrix and vector stored as a 2D list, where
    each component list represents a column vector.

Q3: How will we get there?
A3: Use the linear combination of columns method to multiply matrix and vector.
    I.e. multiply each column of matrix by the corresponding element of vector,
    then sum each resulting vector and return that final resultant vector.

def matrix_vector_multiply(matrix, vector):

  # Initialize a resultant vector full of 0s
  product_vector = []

  for element in matrix[0]:
    append 0 to product_vector

  # Initialize a list to store our intermediate vectors
  inter_vectors = []

  # Calculate the product of each column of matrix with the corresponding
  # element of vector
  for index in range(length(vector)):
    append vector_scalar_multiply(matrix[index], vector[index])
           to inter_vectors

  # Calculate the final result by adding each intermediate vector
  for inter_vector in inter_vectors:
    product_vector = add_vectors(product_vector, inter_vector)

  # Return our product vector
  return product_vector
'''


def matrix_vector_multiply(matrix, vector):

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


# Problem 05
'''
Write an algorithm to implement matrix-matrix multiplication using your
algorithm from Problem #4.

Q1: What do we have?
A1: Two matrices, "left_matrix" and "right_matrix", each stored as a 2D list
    where each component list represents a column vector. Assumed to be
    compatible to multiply.

Q2: What do we want?
A2: A matrix that is the product of left_matrix and right_matrix, stored as a
    2D list where each component list represents a column vector.

Q3: How will we get there?
A3: Create an empty list to represent the resultant matrix, then calculate each
    column using a linear combination of columns and append to the resultant
    matrix.

def matrix_multiply(left_matrix, right_matrix):

  # Define our resultant matrix
  matrix_product = []

  # Calculate each column using linear combination of columns and append to
  # the resultant matrix
  for column in right_matrix:
    append matrix_vector_multiply(left_matrix, column) to matrix_product

  # Return our resultant matrix
  return matrix_product
'''


def matrix_multiply(left_matrix, right_matrix):

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

    '''
    Test Cases
    These could have been rolled into a testing function but I was unsure
    if that would be allowed. They all follow the general format:
    test = func(in1, in2)
    expected = {expected}
    result = test == expected
    print(pass if result, else fail)
    if not result:
        print(expected, test)
    '''

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
