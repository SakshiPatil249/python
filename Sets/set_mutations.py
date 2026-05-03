"""
Problem: Set Mutations
Platform: HackerRank

Description:
You are given a set A and multiple other sets.
You need to perform mutation operations on set A.

Operations:
- update: A = A ∪ other_set
- intersection_update: A = A ∩ other_set
- difference_update: A = A - other_set
- symmetric_difference_update: A = A ⊕ other_set

After performing all operations, print the sum of elements in set A.

Input:
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
...
Output:
38

Approach:
- Parse input and convert to sets
- Apply corresponding mutation based on operation name
- Use built-in set methods for efficiency
- Compute sum at the end


"""

n = int(input())
A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    operation, length = input().split()
    other_set = set(map(int, input().split()))
    
    if operation == "update":
        A.update(other_set)
    elif operation == "intersection_update":
        A.intersection_update(other_set)
    elif operation == "difference_update":
        A.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

print(sum(A))
