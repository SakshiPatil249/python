"""
Problem: Inner and Outer Product
Platform: HackerRank

Description:
Given two arrays A and B:
1. Compute the inner product
2. Compute the outer product

Input:
0 1
2 3

Output:
3
[[0 0]
 [2 3]]

---------------------------------------------------
CONCEPT EXPLANATION
---------------------------------------------------

This problem introduces:
1. Inner Product
2. Outer Product

These are fundamental operations in:
- Linear Algebra
- Machine Learning
- Neural Networks
- Data Science

---------------------------------------------------
1) Inner Product
---------------------------------------------------

Definition:
The inner product multiplies corresponding elements
and adds them together.

Formula:

A · B = a1*b1 + a2*b2 + ...

Example:

A = [0, 1]
B = [2, 3]

Calculation:

(0×2) + (1×3)
= 0 + 3
= 3

Result:
3

NumPy:
np.inner(A, B)


---------------------------------------------------
2) Outer Product
---------------------------------------------------

Definition:
The outer product multiplies every element
of A with every element of B.

Example:

A = [0, 1]
B = [2, 3]

Matrix Formation:

[
 [0×2, 0×3],
 [1×2, 1×3]
]

Result:

[
 [0, 0],
 [2, 3]
]

NumPy:
np.outer(A, B)


---------------------------------------------------
Difference Between Inner and Outer Product
---------------------------------------------------

Inner Product:
- Produces a single value
- Measures similarity/alignment

Outer Product:
- Produces a matrix
- Expands vectors into higher dimensions


---------------------------------------------------
Applications
---------------------------------------------------

Inner Product:
- Similarity calculations
- Neural networks
- Machine learning predictions

Outer Product:
- Matrix construction
- Tensor operations
- Deep learning mathematics

"""

import numpy as np


# ---------------------------------------------------
# Input Arrays
# ---------------------------------------------------
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))


# ---------------------------------------------------
# Inner Product
# ---------------------------------------------------
print(np.inner(A, B))


# ---------------------------------------------------
# Outer Product
# ---------------------------------------------------
print(np.outer(A, B))


# ---------------------------------------------------
# Alternative Approache
# ---------------------------------------------------
"""
1) Inner Product using dot()

np.dot(A, B)

Both produce same result for 1-D arrays.

