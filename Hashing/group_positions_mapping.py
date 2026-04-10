"""
Problem: DefaultDict Tutorial (Group A & B Matching)
Platform: HackerRank

Description:
You are given two groups of words:
- Group A (size sa)
- Group B (size sb)

For each word in Group B, print the positions (1-based index)
where it appears in Group A.

If the word does not exist in Group A, print -1.

Input:
5 2
a
a
b
a
b
a
b

Output:
1 2 4
3 5

Approach:
- Use defaultdict(list) to store positions of each word in Group A
- Iterate through Group A and store indices
- For each word in Group B:
    - Print stored indices if present
    - Else print -1


"""

from collections import defaultdict

sa,sb=map(int,input().split())

ga=defaultdict(list)

for i in range(1,sa+1):
    word=input()
    ga[word].append(i)
    
for i in range(sb):
    word=input()
    
    if word in ga:
        print(*ga[word])
    else:
        print(-1)
    
