"""
Problem: Check Subset
Platform: HackerRank

Description:
For each test case, determine whether set A is a subset of set B.

A is a subset of B if all elements of A are present in B.

Input:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
...

Output:
True
False
False

Approach:
- Convert input lists into sets
- Use built-in method issubset() to check condition

"""

n = int(input())

for _ in range(n):
    len_a = int(input())
    A = set(map(int, input().split()))
    
    len_b = int(input())
    B = set(map(int, input().split()))
    
    print(A.issubset(B))
