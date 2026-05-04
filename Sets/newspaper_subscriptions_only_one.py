"""
Problem: Newspaper Subscriptions (Only One - Not Both)
Platform: HackerRank

Description:
Given two sets:
- English newspaper subscribers
- French newspaper subscribers

Find the number of students who subscribed to either
English or French but NOT both.

Input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Output:
8

Approach:
- Use symmetric difference
- It returns elements present in either set but not both

"""

a = int(input())
e = set(map(int, input().split()))

b = int(input())
f = set(map(int, input().split()))

# Approach 1: Using built-in method
print(len(e.symmetric_difference(f)))

# --------------------------------------------------
# Alternative Approach 
# Using operator '^' for symmetric difference

# print(len(e ^ f))
