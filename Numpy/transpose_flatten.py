"""
Problem: Transpose and Flatten (NumPy)
Platform: HackerRank

Description:
Given a 2D array:
- Print its transpose
- Print its flattened version

Input:
2 2
1 2
3 4

Output:
[[1 3]
 [2 4]]
[1 2 3 4]

Approaches:
1. Using .T and flatten() (recommended)
2. Using np.transpose() and ravel()
3. Using reshape(-1)

"""

import numpy as np


# -------------------------------
# Approach 1: Your Method (Recommended)
# -------------------------------
def transpose_flatten(arr):
    print(arr.T)
    print(arr.flatten())


# -------------------------------
# Approach 2: Using functions
# -------------------------------
def transpose_flatten_alt(arr):
    print(np.transpose(arr))
    print(arr.ravel())


# -------------------------------
# Approach 3: Using reshape
# -------------------------------
def transpose_flatten_reshape(arr):
    print(arr.T)
    print(arr.reshape(-1))


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = np.array([list(map(int, input().split())) for _ in range(n)])

    # Recommended
    transpose_flatten(arr)

    # Alternatives
    # transpose_flatten_alt(arr)
    # transpose_flatten_reshape(arr)
