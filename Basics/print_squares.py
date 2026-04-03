"""
Problem: Print Squares of Numbers
Platform: HackerRank

Description:
Given an integer n, print the square of all non-negative integers less than n.
Each result should be printed on a new line.

Example:
Input: 5
Output:
0
1
4
9
16

Approach:
- Loop from 0 to n-1
- For each number i, print i*i

"""

def print_squares(n):
    for i in range(n):
        print(i * i)


if __name__ == "__main__":
    n = int(input().strip())
    print_squares(n)
