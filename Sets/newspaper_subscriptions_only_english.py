"""
Problem: Newspaper Subscriptions (Only English)
Platform: HackerRank

Description:
Given two sets of student roll numbers:
- English newspaper subscribers
- French newspaper subscribers

Find the total number of students who are subscribed
to ONLY the English newspaper.

Input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Output:
4

Approach:
- Convert both lists into sets
- Use difference operation (A - B)
- Count remaining elements


"""


def count_only_english():
    _ = int(input().strip())
    english = set(map(int, input().split()))

    _ = int(input().strip())
    french = set(map(int, input().split()))

    # Students only in English
    only_english = len(english.difference(french))

    print(only_english)


if __name__ == "__main__":
    count_only_english()
