"""
Problem: Linear Algebra - Determinant
Platform: HackerRank

Description:
Given a square matrix, compute its determinant.

Round the answer to 2 decimal places.

Input:
2
1.1 1.1
1.1 1.1

Output:
0.0

Approaches:
Using np.linalg.det()

"""

import numpy as np

# -------------------------------
# Approach : Using NumPy 
# -------------------------------
def determinant_numpy(arr):
    d = np.linalg.det(arr)
    return round(d, 2)


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    n = int(input())
    arr = np.array([list(map(float, input().split())) for _ in range(n)])
    print(determinant_numpy(arr))

 
