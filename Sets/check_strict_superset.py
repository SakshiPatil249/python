"""
Problem: Check Strict Superset
Platform: HackerRank

Description:
Given a set A, check whether it is a strict superset
of all other given sets.

A is a strict superset of B if:
- All elements of B are in A
- AND A has more elements than B

Input:
Set A
Number of other sets
Other sets...

Output:
True / False

Approach:
- For each set:
    - Check if A is a strict superset using '>'
- If any check fails → False

"""

a = set(map(int, input().split()))
n = int(input())

r = True
for i in range(n):
    other = set(map(int, input().split()))
    
    # Check strict superset
    if not a > other:
        r = False
        break
        
print(r)

# --------------------------------------------------
# Alternative Approach (using issuperset + length check)

# r = True
# for _ in range(n):
#     other = set(map(int, input().split()))
#     if not (a.issuperset(other) and len(a) > len(other)):
#         r = False
#         break
# print(r)
