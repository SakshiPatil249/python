"""
Problem: Text Wrap
Platform: HackerRank

Description:
Given a string and a width, wrap the string into lines
such that each line has a maximum width.

Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

Approach:
1. Use Python's textwrap module to wrap text automatically
2. Manually slice the string in chunks of max_width


"""



    """
    Approach 1: Using textwrap (recommended)
    """
import textwrap

def wrap(string, max_width):

    return textwrap.fill(string, max_width)



    """
    Approach 2: Manual slicing
    """

def wrap_manual(string, max_width):

    result = ""

    for i in range(0, len(string), max_width):
        result += string[i:i + max_width] + "\n"

    return result.rstrip()  # remove last newline


if __name__ == "__main__":
    string = input().strip()
    max_width = int(input().strip())

    # Recommended method
    print(wrap(string, max_width))

    # Uncomment to test manual method
    # print(wrap_manual(string, max_width))
