"""
Problem: Mean, Variance and Standard Deviation
Platform: HackerRank

Description:
Given a 2D NumPy array:
- Find mean along axis 1
- Find variance along axis 0
- Find standard deviation of entire array

Input:
2 2
1 2
3 4

Output:
[1.5 3.5]
[1. 1.]
1.11803398875

Approaches:
1. Using NumPy statistical functions (recommended)
2. Using chained operations

"""

import numpy as np


# -------------------------------
# Approach 1: Your Method (Corrected)
# -------------------------------
def statistics_operations(arr):
    # Mean row-wise
    print(np.mean(arr, axis=1))

    # Variance column-wise
    print(np.var(arr, axis=0))

    # Standard deviation of entire array
    print(round(np.std(arr, axis=None),11))


# -------------------------------
# Approach 2: Compact version
# -------------------------------
def statistics_compact(arr):
    print(arr.mean(axis=1))
    print(arr.var(axis=0))
    print(arr.std())



# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = np.array([list(map(int, input().split())) for _ in range(n) ])
    # Recommended
    statistics_operations(arr)

    # Alternative
    # statistics_compact(arr)
