"""
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 

For Problems #0-5 from HW01, Do the following.



1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 

3) Test each of your functions on at least 2 inputs. 

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""


#Example:

#Problem 00

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

def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result

#End Example



# Problem 01
'''
Write an algorithm to implement scalar-vector multiplication.

Q1: What do we have?
A1: A vector "vector" stored as a list and a scalar "scalar" stored as an integer

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
        matrix_sum.append(vector_add(matrix_a[index], matrix_b[index]))
    
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
    append vector_scalar_multiply(matrix[index], vector[index]) to inter_vectors

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
        inter_vectors.append(vector_scalar_multiply(matrix[index], vector[index]))
    
    # Calculate the final result by adding each intermediate vector
    for inter_vector in inter_vectors:
        product_vector = vector_add(product_vector, inter_vector)
    
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
    
    # Test cases
    # TODO: These technically go over the 80 character style guide limit...
    # Could clean up with shorter variable names? Split into separate lines?
    # Could use unittest module or create a special test function?
    # Or just say whatever to PEP8 and go over 80 characters anyway

    # add_vectors(test_vector_a, test_vector_b) should output [4, 3, 6]
    print(f'add_vectors test #1: {add_vectors(vector_a, vector_b)}')
    print(f'Expected result:     {[4, 3, 6]}')
    # add_vectors(test_vector_a, test_vector_c) should output [6, 2, 7]
    print(f'add_vectors test #2: {add_vectors(vector_a, vector_b)}')
    print(f'Expected result:     {[6, 2, 7]}')

    # vector_scalar_multiply(vector_a, scalar_a) should output [4, 8, 16]
    print(f'vector_scalar_multiply test #1: {vector_scalar_multiply(vector_a, scalar_a)}')
    print(f'Expected result:                {[4, 8, 16]}')
    # vector_scalar_multiply(vector_b, scalar_b) should output [21, 7, 14]
    print(f'vector_scalar_multiply test #2: {vector_scalar_multiply(vector_b, scalar_b)}')
    print(f'Expected result:                {[21, 7, 14]}')

    # matrix_scalar_multiply(matrix_a, scalar_a) should output [[4, 32, 16], [32, 28, 24], [12, 0, 36]]
    print(f'matrix_scalar_multiply test #1: {matrix_scalar_multiply(matrix_a, scalar_a)}')
    print(f'Expected result:                {[[4, 32, 16], [32, 28, 24], [12, 0, 36]]}')
    # matrix_scalar_multiply(matrix_b, scalar_b) should output [[35, 42, 14], [7, 49, 0], [28, 49, 49]]
    print(f'matrix_scalar_multiply test #2: {matrix_scalar_multiply(matrix_b, scalar_b)}')
    print(f'Expected result:                {[[35, 42, 14], [7, 49, 0], [28, 49, 49]]}')
    
    # matrix_add

    # matrix_vector_multiply

    # matrix_matrix_multiply

