def vector_add(vector_a,vector_b):
    '''
    Input:  vector_a, vector_b: two vectors stored as lists. 
            Assumed to be the same length.

    Output: The sum of vector_a and vector_b stored as a list.

    Method: We will create an empty list and append the sums of the
    corresponding elements of vector_a and vector_b. 
    '''
   
    # Initializing result as an empty list
    result = []

    # Set each element of result to be equal to the desired sum.
    for index in range(len(vector_a)):
        result.append(vector_a[index] + vector_b[index])
    
    # Return the desired result.
    return result


def vector_scalar_multiply(vector, scalar):
    '''
    Input:  vector: A vector stored as a list 
            scalar: A scalar stored as a number
    
    Output: The product of vector and scalar stored as a list
    
    Method: Create an empty list and then store vector times scalar by
            appending, in order, the scalar multiplied by each element of
            vector
    '''

    # Create a new list to server as our resultant vector
    product_vector = []
    
    # Compute the product by calculating each element then append it to result
    for element in vector:
        product_vector.append(element * scalar)

    # Return our product vector
    return product_vector
 

def matrix_scalar_multiply(matrix, scalar):
    '''
    Input:  matrix: A matrix stored as a 2D list where each component list
                represents a vector
            scalar: A scalar stored as a number
    
    Output: The product of matrix and scalar, stored as a 2D list, where each
            component list represents a vector, similar to the input matrix
    
    Method: Create an empty list then append, in order, each component vector
            of matrix multiplied by the scalar using vector_scalar_multiply()
    '''

    # Create a new list to serve as our resultant matrix
    product_matrix = []
    
    # Compute the product by calculating the product of each vector times the
    # scalar, and appending it to our result
    for vector in matrix:
        product_matrix.append(vector_scalar_multiply(vector, scalar))
    
    # Return our product matrix
    return product_matrix


def matrix_add(matrix_a, matrix_b):
    '''
    Input:  matrix_a, matrix_b: Two matrices stored as 2D lists, where each
                component list represents vectors of the same type as each
                other (rows/rows, or columns/columns). Assumed to be the same
                size.
    
    Output: The sum of matrix_a and matrix_b, stored as a 2D list, where each
                component list represents a vector of the same type as the
                input matrices (rows or columns).
    
    Method: Create an empty list then append, in order, the sum of each 
            corresponding component vector of matrix_a and matrix_b using
            vector_add()
    '''
    # Create a new list to server as our resultant matrix
    matrix_sum = []
    
    # Compute the sum by calculating the sum of each pair of corresponding
    # vectors in matrix_a and matrix_b
    for index in range(len(matrix_a)):
        matrix_sum.append(vector_add(matrix_a[index], matrix_b[index]))
    
    # Return our sum matrix
    return matrix_sum


def matrix_vector_multiply(matrix, vector):
    '''
    Input:  A matrix "matrix" stored as a 2D list, where each component list
            represents a column vector, and a column vector "vector", stored
            as a list. Assumed to be compatible to multiply.
    
    Output: The matrix-vector product of matrix and vector stored as a list,
            where matrix is the left operand and vector the right.
    
    Method: Use the linear combination of columns method to multiply matrix and
            vector. I.e. multiply each column of matrix by the corresponding 
            element of vector, store those vectors, finally, sum each resulting
            vector and return that final vector.
    '''
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


def matrix_multiply(left_matrix, right_matrix):
    '''
    Input:  left_matrix, right_matrix: Two matrices, each stored as a 2D list
            where each component list represents a column vector. Assumed to be
            compatible to multiply.
    
    Output: A matrix that is the product of left_matrix and right_matrix,
            stored as a 2D list where each component list represents a column
            vector.
    
    Method: Create an empty list to represent the resultant matrix, then
            calculate each column using matrix_vector_multiply(), appending to
            the resultant matrix as they are calculated.
    '''

    # Define our resultant matrix
    matrix_product = []
    
    # Calculate each column using linear combination of columns and append to
    # the resultant matrix
    for column in right_matrix:
        matrix_product.append(matrix_vector_multiply(left_matrix, column))
    
    # Return our resultant matrix
    return matrix_product

