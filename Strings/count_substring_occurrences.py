"""
Problem: Count Substring Occurrences
Platform: HackerRank

Description:
Given a string and a substring, count how many times
the substring occurs in the string (including overlapping occurrences).

Input:
ABCDCDC
CDC

Output:
2

Approach:
- Traverse the string from left to right
- Extract substring of length equal to sub_string
- Compare and count matches (including overlaps)

"""


def count_substring(string, sub_string):
    count = 0
    n = len(string)
    m = len(sub_string)

    # Slide window of size m across string
    for i in range(n - m + 1):
        if string[i:i + m] == sub_string:
            count += 1

    return count


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    print(count_substring(string, sub_string))
