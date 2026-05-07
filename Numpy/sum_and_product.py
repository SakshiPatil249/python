"""
Problem: Sum and Product (NumPy)
Platform: HackerRank

Description:
Given a 2D NumPy array:
1. Find the sum along axis 0
2. Find the product of that result

Input:
2 2
1 2
3 4

Output:
24

Approaches:
1. Using np.sum() + np.prod() (recommended)
2. Using chained operations

"""

import numpy as np


# -------------------------------
# Approach 1: (Recommended)
# -------------------------------
def sum_product(arr):
    col_sum = np.sum(arr, axis=0)
    return np.prod(col_sum)


# -------------------------------
# Approach 2: Compact version
# -------------------------------
def sum_product_compact(arr):
    return np.prod(np.sum(arr, axis=0))


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = np.array([list(map(int, input().split())) for _ in range(n) ])

    # Recommended
    print(sum_product(arr))

    # Alternative
    # print(sum_product_compact(arr))
