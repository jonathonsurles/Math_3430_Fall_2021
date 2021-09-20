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


# Problem 02


# Problem 03


# Problem 04


# Problem 05



# Test if file run directly
if __name__ == '__main__':
    
    # Variables for testing
    scalar_a = 4
    scalar_b = 7
    vector_a = [1, 2, 4]
    vector_b = [3, 1, 2]
    vector_c = [5, 0, 3]
    
    # Test cases
    # add_vectors(test_vector_a, test_vector_b) should output [4, 3, 6]
    print(f'add_vectors test #1: {(add_vectors(test_vector_a, test_vector_b))}')
    print(f'Expected result: {[4, 3, 6]}')
    # add_vectors(test_vector_a, test_vector_c) should output [6, 2, 7]
    print(f'add_vectors test #2: {(add_vectors(test_vector_a, test_vector_b))}')
    print(f'Expected result: {[6, 2, 7]}')

