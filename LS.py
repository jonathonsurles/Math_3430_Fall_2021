"""Contains functions to find the least squares solutions of equations."""


import LA
import QR


# Type aliases
Vector = list[complex]
Matrix = list[list[complex]]


def least_squares(matrix: Matrix, vector: Vector) -> Vector:
    """Finds the least squares solution of a matrix-vector product, Ax = b

    ...

    Args:
        matrix: The matrix A in an equation Ax = b
        vector: The vector b in an equation Ax = b

    Returns:
        The vector x in an equation Ax = b
    """
    '''Plan
    Let Q, R such that QR = A and R is upper triangular and square
    Calculate the vector c = Q*b, which is equal to Rx
    Create an empty vector of the appropriate size to store x
    Use back subsitution to find the elements of x, since R is triangular
    Return R
    '''
