"""
Problem: Array Mathematics (NumPy)
Platform: HackerRank

Description:
Perform element-wise operations on two NumPy arrays:
1. Addition
2. Subtraction
3. Multiplication
4. Floor Division
5. Modulus
6. Power

Input:
1 4
1 2 3 4
5 6 7 8

Output:
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]

"""

import numpy as np

# -------------------------------
# Approach 1: Using NumPy functions 
# -------------------------------
def array_math(A, B):
    print(np.add(A, B))
    print(np.subtract(A, B))
    print(np.multiply(A, B))
    print(np.floor_divide(A, B))
    print(np.mod(A, B))
    print(np.power(A, B))


# -------------------------------
# Approach 2: Using operators
# -------------------------------
def array_math_operators(A, B):
    print(A + B)
    print(A - B)
    print(A * B)
    print(A // B)
    print(A % B)
    print(A ** B)


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    n, m = map(int, input().split())

    A = np.array([
        list(map(int, input().split()))
        for _ in range(n)
    ])

    B = np.array([
        list(map(int, input().split()))
        for _ in range(n)
    ])

    # Recommended
    array_math(A, B)

    # Alternative
    # array_math_operators(A, B)
