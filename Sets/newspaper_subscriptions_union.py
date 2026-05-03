"""
Problem: No Idea! / Newspaper Subscriptions (Union)
Platform: HackerRank

Description:
Given two sets of student roll numbers:
- One set for English newspaper subscribers
- One set for French newspaper subscribers

Find the total number of students who have subscribed to
at least one newspaper.

Input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Output:
13

Approach:
- Convert both lists into sets
- Use union operation to combine unique elements
- Count total elements using len()


"""


def count_subscriptions():
    _ = int(input().strip())  # number of English subscribers
    english = set(map(int, input().split()))

    _ = int(input().strip())  # number of French subscribers
    french = set(map(int, input().split()))

    # Union gives all unique students
    total_students = len(english.union(french))

    print(total_students)


if __name__ == "__main__":
    count_subscriptions()
