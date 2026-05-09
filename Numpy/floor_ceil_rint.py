"""
Problem: Floor, Ceil and Rint
Platform: HackerRank

Description:
Given a 1-D NumPy array, print:
1. Floor values
2. Ceil values
3. Rounded values using rint()

Input:
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

Output:
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[ 2.  3.  4.  5.  6.  7.  8.  9. 10.]
[ 1.  2.  3.  4.  6.  7.  8.  9. 10.]

---------------------------------------------------
CONCEPT EXPLANATION
---------------------------------------------------

This problem demonstrates:
1. floor()
2. ceil()
3. rint()

These are important mathematical operations
used in:
- Data Science
- Machine Learning
- Numerical Computing

---------------------------------------------------
1) np.floor()
---------------------------------------------------

Returns the greatest integer
LESS THAN OR EQUAL to the number.

Examples:

floor(2.9) = 2
floor(5.1) = 5
floor(-2.3) = -3

Notice:
Negative values go DOWN.

Example:
-2.3 -> -3


---------------------------------------------------
2) np.ceil()
---------------------------------------------------

Returns the smallest integer
GREATER THAN OR EQUAL to the number.

Examples:

ceil(2.1) = 3
ceil(5.9) = 6
ceil(-2.3) = -2

Notice:
Negative values go UP.


---------------------------------------------------
3) np.rint()
---------------------------------------------------

Rounds to nearest integer.

Examples:

rint(2.3) = 2
rint(2.7) = 3
rint(5.5) = 6

Used for:
- Approximation
- Data preprocessing
- Numerical rounding


---------------------------------------------------
IMPORTANT LINE
---------------------------------------------------

np.set_printoptions(legacy='1.13')

This ensures HackerRank output formatting
matches expected output exactly.


---------------------------------------------------
Time Complexity
---------------------------------------------------

O(n)

---------------------------------------------------
Space Complexity
---------------------------------------------------

O(n)
"""

import numpy as np

# Important for HackerRank formatting
np.set_printoptions(legacy='1.13')


# -----------------------------------
# Input Array
# -----------------------------------
A = np.array(
    list(map(float, input().split()))
)


# -----------------------------------
# Floor Values
# -----------------------------------
print(np.floor(A))


# -----------------------------------
# Ceil Values
# -----------------------------------
print(np.ceil(A))


# -----------------------------------
# Rounded Values
# -----------------------------------
print(np.rint(A))

