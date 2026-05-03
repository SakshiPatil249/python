"""
Problem: Newspaper Subscriptions (Intersection)
Platform: HackerRank

Description:
Given two sets of student roll numbers:
- English newspaper subscribers
- French newspaper subscribers

Find the total number of students who have subscribed
to both newspapers.

Input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Output:
5

Approach:
- Convert both lists into sets
- Use intersection operation to find common elements
- Count them using len()


"""


def count_common_subscriptions():
    _ = int(input().strip())
    english = set(map(int, input().split()))

    _ = int(input().strip())
    french = set(map(int, input().split()))

    # Intersection gives common students
    common_students = len(english.intersection(french))

    print(common_students)


if __name__ == "__main__":
    count_common_subscriptions()
