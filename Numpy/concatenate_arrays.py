"""
Problem: Concatenate Arrays (NumPy)
Platform: HackerRank

Description:
Given two arrays A and B with same number of columns,
concatenate them along axis 0 (row-wise).

Input:
4 3 2
(A matrix)
(B matrix)

Output:
Combined array

Approaches:
1. Using np.concatenate() (recommended)
2. Using np.vstack()
3. Using np.r_ shortcut

"""

import numpy as np


# -------------------------------
# Approach 1: Using concatenate() 
# -------------------------------
def concat_arrays(A, B):
    return np.concatenate((A, B), axis=0)


# -------------------------------
# Approach 2: Using vstack()
# -------------------------------
def concat_vstack(A, B):
    return np.vstack((A, B))


# -------------------------------
# Approach 3: Using np.r_
# -------------------------------
def concat_r(A, B):
    return np.r_[A, B]


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    n, m, c = map(int, input().split())

    A = np.array([list(map(int, input().split())) for _ in range(n)])
    B = np.array([list(map(int, input().split())) for _ in range(m)])

    # Recommended
    print(concat_arrays(A, B))

    # Alternate ways
    # print(concat_vstack(A, B))
    # print(concat_r(A, B))
