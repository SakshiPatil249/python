"""
Problem: Polynomial Evaluation (NumPy)
Platform: HackerRank

Description:
Given coefficients of a polynomial and a value x,
compute the polynomial value at x.

Input:
1.1 2 3
0

Output:
3.0

Approaches:
1. Using np.polyval() (recommended)
2. Manual computation using loop
3. Using Horner’s Method (optimized)


"""

import numpy as np


# -------------------------------
# Approach 1: Using np.polyval() 
# -------------------------------
def evaluate_poly(coeff, x):
    return np.polyval(coeff, x)


# -------------------------------
# Approach 2: Manual computation
# -------------------------------
def evaluate_manual(coeff, x):
    n = len(coeff)
    result = 0
    for i in range(n):
        result += coeff[i] * (x ** (n - i - 1))
    return result


# -------------------------------
# Approach 3: Horner’s Method (Best for interviews)
# -------------------------------
def evaluate_horner(coeff, x):
    result = 0
    for c in coeff:
        result = result * x + c
    return result


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    coeff = list(map(float, input().split()))
    x = float(input())

    # Recommended
    print(evaluate_poly(coeff, x))

    # Alternatives
    # print(evaluate_manual(coeff, x))
    # print(evaluate_horner(coeff, x))
