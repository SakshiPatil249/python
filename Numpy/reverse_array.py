"""
Problem: Arrays (NumPy)
Platform: HackerRank

Description:
Given a list of space-separated numbers, convert them
into a NumPy array of floats and print the array in reverse order.

Input:
1 2 3 4 -8 -10

Output:
[-10.  -8.   4.   3.   2.   1.]

Approaches:
1. Slicing (recommended)
2. NumPy flip()
3. Python reversed() + conversion

"""

import numpy as np


# -------------------------------
# Approach 1: Slicing (Best)
# -------------------------------
def arrays(arr):
    arr = np.array(arr, dtype=float)
    return arr[::-1]


# -------------------------------
# Approach 2: Using np.flip()
# -------------------------------
def arrays_flip(arr):
    arr = np.array(arr, dtype=float)
    return np.flip(arr)


# -------------------------------
# Approach 3: Using reversed()
# -------------------------------
def arrays_reversed(arr):
    arr = np.array(list(reversed(arr)), dtype=float)
    return arr


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    arr = input().strip().split()

    # Recommended
    print(arrays(arr))

    # Uncomment to test alt
    # print(arrays_flip(arr))
    # print(arrays_reversed(arr))
