"""
Problem: Shape and Reshape (NumPy)
Platform: HackerRank

Description:
Given 9 space-separated integers, convert them into a 3x3 NumPy array.

Input:
1 2 3 4 5 6 7 8 9

Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Approaches:
1. Using reshape()
2. Using np.array with nested lists
3. Using np.reshape() function


"""

import numpy as np


# -------------------------------
# Approach 1: Using reshape() (Recommended)
# -------------------------------
def reshape_array(arr):
    arr = np.array(arr, dtype=int)
    return arr.reshape(3, 3)


# -------------------------------
# Approach 2: Using np.reshape()
# -------------------------------
def reshape_array_func(arr):
    arr = np.array(arr, dtype=int)
    return np.reshape(arr, (3, 3))


# -------------------------------
# Approach 3: Manual grouping
# -------------------------------
def reshape_manual(arr):
    arr = list(map(int, arr))
    matrix = [
        arr[0:3],
        arr[3:6],
        arr[6:9]
    ]
    return np.array(matrix)


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    arr = input().strip().split()

    # Recommended
    print(reshape_array(arr))

    # Uncomment to test alt
    # print(reshape_array_func(arr))
    # print(reshape_manual(arr))
