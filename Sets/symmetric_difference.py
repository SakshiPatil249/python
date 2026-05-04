"""
Problem: Symmetric Difference
Platform: HackerRank

Description:
Given two sets of integers, print the symmetric difference
in ascending order.

Symmetric difference = elements present in either set,
but not in both.

Input:
4
2 4 5 9
4
2 4 11 12

Output:
5
9
11
12

Approach:
- Convert inputs into sets
- Use symmetric difference operation (A ^ B)
- Sort the result
- Print each element on a new line

"""


def symmetric_difference():
    _ = int(input().strip())
    set_a = set(map(int, input().split()))

    _ = int(input().strip())
    set_b = set(map(int, input().split()))

    # Elements in either A or B but not both
    result = set_a.symmetric_difference(set_b)

    for num in sorted(result):
        print(num)


if __name__ == "__main__":
    symmetric_difference()
