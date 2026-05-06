"""
Problem: Zeros and Ones (NumPy)
Platform: HackerRank

Description:
Given a shape (dimensions), create:
1. An array of zeros
2. An array of ones

Both should be of integer type.

Input:
3 3 3

Output:
3D arrays of zeros and ones

Approaches:
1. Using np.zeros() and np.ones() (recommended)
2. Using np.full()

"""

import numpy as np


# -------------------------------
# Approach 1: zeros() and ones() 
# -------------------------------
def zeros_ones(shape):
    print(np.zeros(shape, dtype=int))
    print(np.ones(shape, dtype=int))


# -------------------------------
# Approach 2: Using np.full()
# -------------------------------
def zeros_ones_full(shape):
    print(np.full(shape, 0, dtype=int))
    print(np.full(shape, 1, dtype=int))



# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    shape = tuple(map(int, input().split()))

    # Recommended
    zeros_ones(shape)

    # Alternative
    # zeros_ones_full(shape)
