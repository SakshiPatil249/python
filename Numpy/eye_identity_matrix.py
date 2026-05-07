"""
Problem: Eye and Identity (NumPy)
Platform: HackerRank

Description:
Print an array with:
- 1s on the main diagonal
- 0s elsewhere

Input:
3 3

Output:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

Approaches:
1. Using np.eye() (recommended)
2. Using np.identity()
3. Manual creation

"""

import numpy as np

# Important for HackerRank formatting
np.set_printoptions(legacy='1.13')


# -------------------------------
# Approach 1: Using np.eye() (Your method)
# -------------------------------
def eye_matrix(n, m):
    return np.eye(n, m)


# -------------------------------
# Approach 2: Using np.identity()
# Only works for square matrices
# -------------------------------
def identity_matrix(n):
    return np.identity(n)


# -------------------------------
# Approach 3: Manual creation
# -------------------------------
def manual_eye(n, m):
    arr = np.zeros((n, m))

    for i in range(min(n, m)):
        arr[i][i] = 1

    return arr


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    n, m = map(int, input().split())

    # Recommended
    print(eye_matrix(n, m))

    # Alternatives
    # if n == m:
    #     print(identity_matrix(n))

    # print(manual_eye(n, m))
