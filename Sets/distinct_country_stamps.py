"""
Problem: Set - Add() (Distinct Country Stamps)
Platform: HackerRank

Description:
Given a list of country names (stamps), find the total number
of distinct countries.

Input:
7
UK
China
USA
France
New Zealand
UK
France

Output:
5

Approach:
- Use a set to store unique country names
- Add each input to the set
- Print the size of the set


"""


def count_distinct_stamps():
  n = int(input())
  s = set()
  for i in range(n):
      s.add(input())
  print(len(s))

if __name__ == "__main__":
    count_distinct_stamps()
