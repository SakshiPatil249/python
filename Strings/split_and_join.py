"""
Problem: Split and Join
Platform: HackerRank

Description:
Given a string of space-separated words, split the string
and join the words using a hyphen (-).

Input:
this is a string

Output:
this-is-a-string

Approach:
1. Use split() to break string into words
2. Use join() to combine words with '-'

"""

    """
    Approach 1: Optimized Pythonic solution
    """
def split_and_join(line):

    return "-".join(line.split())


    """
    Approach 2: Step-by-step method
    """
def split_and_join_basic(line):

    words = line.split(" ")
    result = "-".join(words)
    return result


if __name__ == "__main__":
    line = input().strip()

    # Recommended method
    print(split_and_join(line))

    # Uncomment to test
    # print(split_and_join_basic(line))
