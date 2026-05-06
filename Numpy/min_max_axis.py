"""
Problem: Min and Max (NumPy)
Platform: HackerRank

Description:
Given a 2D NumPy array:
- Find the minimum value along axis 1 (row-wise)
- Then print the maximum of those values

Input:
4 2
2 5
3 7
1 3
4 0

Output:
3

Approaches:
1. Using np.min + np.max (recommended)
2. Using chained operations
3. Using Python built-ins

"""

import numpy as np


# -------------------------------
# Approach 1: Step-by-step (Your method)
# -------------------------------
def min_max(arr):
    row_min = np.min(arr, axis=1)
    return np.max(row_min)


# -------------------------------
# Approach 2: Chained (Compact)
# -------------------------------
def min_max_compact(arr):
    return np.max(np.min(arr, axis=1))


# -------------------------------
# Approach 3: Without NumPy (for understanding)
# -------------------------------
def min_max_python(arr):
    row_min = [min(row) for row in arr]
    return max(row_min)


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = np.array([list(map(int, input().split())) for _ in range(n)])

    # Recommended
    print(min_max(arr))

    # Alternatives
    # print(min_max_compact(arr))
    # print(min_max_python(arr.tolist()))
