"""
Problem: Designer Door Mat
Platform: HackerRank

Description:
Print a decorative door mat pattern using:
- .|.
- WELCOME
- -

Conditions:
1. Size = N x M
2. N is odd
3. M = 3 * N

Example Input:
9 27

Example Output:
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

---------------------------------------------------
CONCEPT EXPLANATION
---------------------------------------------------

This problem focuses on:
1. Pattern printing
2. String multiplication
3. String centering
4. Loops

---------------------------------------------------
1) String Multiplication
---------------------------------------------------

In Python:

".|." * 3

Produces:

".|..|..|."

This helps create repeating patterns easily.


---------------------------------------------------
2) center(width, fillchar)
---------------------------------------------------

Syntax:
string.center(width, fillchar)

Example:

"WELCOME".center(27, "-")

Output:

"----------WELCOME----------"

It:
- Places the text in center
- Fills remaining space using '-'


---------------------------------------------------
3) Pattern Logic
---------------------------------------------------

Top Half:
-------------
Pattern count increases by 2:

1
3
5
7
...

Example:
".|." * 3

Middle:
--------
"WELCOME" at center

Bottom Half:
-------------
Mirror image of top half


---------------------------------------------------
---------------------------------------------------

1. Using center() 
"""

# -----------------------------------
# Approach 1: Using center() 
# -----------------------------------

n, m = map(int, input().split())

# Top Half
for i in range(1, n, 2):

    # Create repeated pattern
    pattern = ".|." * i

    # Center align using '-'
    print(pattern.center(m, "-"))


# Middle Part
print("WELCOME".center(m, "-"))


# Bottom Half
for i in range(n - 2, 0, -2):

    # Create repeated pattern
    pattern = ".|." * i

    # Center align using '-'
    print(pattern.center(m, "-"))


