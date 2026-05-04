"""
Problem: Captain's Room
Platform: HackerRank

Description:
Given room numbers where:
- Each family room appears k times
- Captain's room appears only once

Find the Captain's room number.

Input:
5
1 2 3 6 5 4 ...

Output:
8

Approach 1:
- Count frequency using Counter
- Find element with frequency 1

Approach 2 (Optimized):
- Use mathematical formula:
    (sum(unique) * k - sum(all)) // (k - 1)

"""

from collections import Counter


# -------------------------------
# Approach 1: Using Counter
# -------------------------------
def captain_room_counter():
    k = int(input().strip())
    rooms = list(map(int, input().split()))

    freq = Counter(rooms)

    for room, cnt in freq.items():
        if cnt == 1:
            print(room)
            break


# -------------------------------
# Approach 2: Optimized Math Trick
# -------------------------------
def captain_room_optimized():
    k = int(input().strip())
    rooms = list(map(int, input().split()))

    unique_rooms = set(rooms)

    captain = (sum(unique_rooms) * k - sum(rooms)) // (k - 1)
    print(captain)


if __name__ == "__main__":
    # Use one of the methods:

    # captain_room_counter()      # Simple & clear
    captain_room_optimized()     # Recommended (interview-level)
