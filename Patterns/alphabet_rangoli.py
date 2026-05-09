"""
Problem: Alphabet Rangoli
Platform: HackerRank

Description:
Print an alphabet rangoli pattern of given size.

A rangoli is a symmetric alphabet pattern.

Example for size = 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

---------------------------------------------------
CONCEPT EXPLANATION
---------------------------------------------------

This problem focuses on:
1. String slicing
2. Pattern printing
3. Symmetry
4. String joining
5. String centering

---------------------------------------------------
1) string.ascii_lowercase
---------------------------------------------------

Python provides lowercase alphabets using:

string.ascii_lowercase

Example:

abcdefghijklmnopqrstuvwxyz

This helps us access letters easily.


---------------------------------------------------
2) Width Formula
---------------------------------------------------

Width of rangoli:

width = 4 * size - 3

Example:
size = 5

width = 4(5) - 3
= 17

This ensures proper center alignment.


---------------------------------------------------
3) Pattern Logic
---------------------------------------------------

For each row:
- Left side decreases
- Right side increases
- Join letters using '-'

Example:

e-d-c-b-a-b-c-d-e

This creates symmetry.


---------------------------------------------------
4) String Joining
---------------------------------------------------

"-".join(sequence)

Example:

["e", "d", "c"]

Becomes:

"e-d-c"


---------------------------------------------------
5) center(width, '-')
---------------------------------------------------

Used to align pattern in center.

Example:

"e-d-e".center(17, "-")

Output:

"------e-d-e------"


---------------------------------------------------
6) Final Construction
---------------------------------------------------

Top half:
lines[::-1]

Bottom half:
lines[1:]

Combined:
Top + Bottom


"""

import string

# All lowercase alphabets
alpha = string.ascii_lowercase


# ---------------------------------------------------
# Function to Print Rangoli
# ---------------------------------------------------
def print_rangoli(size):

    # Total width of rangoli
    width = 4 * size - 3

    # Store all rows
    lines = []

    # Generate upper half including middle row
    for i in range(size):

        # Left decreasing part
        left = alpha[size - 1:i:-1]

        # Right increasing part
        right = alpha[i:size]

        # Combine both parts
        row = "-".join(left + right)

        # Center align using '-'
        lines.append(row.center(width, "-"))

    # Print full rangoli
    # Top half reversed + bottom half
    print("\n".join(lines[::-1] + lines[1:]))


# ---------------------------------------------------
# Main Execution
# ---------------------------------------------------
if __name__ == '__main__':

    n = int(input())

    print_rangoli(n)


