"""
Problem: Matrix Multiplication
Platform: HackerRank

Description:
Given two N x N matrices, compute their matrix product.

Input:
2
1 2
3 4
1 2
3 4

Output:
[[ 7 10]
 [15 22]]

---------------------------------------------------
CONCEPT EXPLANATION
---------------------------------------------------

1) Dot Product
----------------
The dot product is performed between two vectors.

Formula:

A · B = a1*b1 + a2*b2 + a3*b3 + ...

Example:
A = [1, 2, 3]
B = [4, 5, 6]

Dot Product:
(1×4) + (2×5) + (3×6)
= 4 + 10 + 18
= 32

NumPy:
np.dot(A, B)

Result:
32

Used in:
- Machine Learning
- Similarity calculations
- Neural networks


2) Cross Product
-----------------
The cross product works only for 3D vectors.

It returns a vector perpendicular to both vectors.

Example:
A = [1, 0, 0]
B = [0, 1, 0]

NumPy:
np.cross(A, B)

Result:
[0 0 1]

Used in:
- Physics
- 3D graphics
- Rotations


3) Matrix Product (This Problem)
---------------------------------
Matrix multiplication is done by:
- Taking rows from first matrix
- Multiplying with columns from second matrix

Example:

A =
[[1 2]
 [3 4]]

B =
[[1 2]
 [3 4]]

First element:
(1×1) + (2×3)
= 1 + 6
= 7

Final result:
[[ 7 10]
 [15 22]]

Important Rule:
(Number of columns in A)
must equal
(Number of rows in B)

NumPy Methods:
1. np.dot(A, B)
2. A @ B
3. np.matmul(A, B)

"""

import numpy as np


# -----------------------------------
# Approach 1: Using np.dot()
# -----------------------------------
def matrix_product_dot(A, B):
    return np.dot(A, B)


# -----------------------------------
# Approach 2: Using @ operator
# -----------------------------------
def matrix_product_operator(A, B):
    return A @ B


# -----------------------------------
# Approach 3: Using np.matmul()
# -----------------------------------
def matrix_product_matmul(A, B):
    return np.matmul(A, B)


# -----------------------------------
# Main Execution
# -----------------------------------
if __name__ == "__main__":

    # Input size of square matrix
    n = int(input())

    # First matrix
    A = np.array([
        list(map(int, input().split()))
        for _ in range(n)
    ])

    # Second matrix
    B = np.array([
        list(map(int, input().split()))
        for _ in range(n)
    ])

    # Recommended approach
    print(matrix_product_dot(A, B))

    # Alternative methods
    # print(matrix_product_operator(A, B))
    # print(matrix_product_matmul(A, B))
