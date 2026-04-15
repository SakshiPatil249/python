"""
Problem: Text Alignment (H Pattern)
Platform: HackerRank

Description:
Print the alphabet 'H' in a specific pattern using a given thickness.

Input:
5

Output:
(H pattern as shown)

Approach:
- Use string multiplication and alignment functions:
    - center()
    - ljust()
    - rjust()
- Divide pattern into 5 parts:
    1. Top Cone
    2. Top Pillars
    3. Middle Belt
    4. Bottom Pillars
    5. Bottom Cone

"""


def print_h_pattern(thickness):
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c * (2 * i + 1)).center(2 * thickness - 1))

    # Top Pillars
    for _ in range(thickness + 1):
        print((c * thickness).center(2 * thickness - 1) +
              (c * thickness).center(6 * thickness - 1))

    # Middle Belt
    for _ in range((thickness + 1) // 2):
        print((c * (thickness * 5)).center(6 * thickness - 1))

    # Bottom Pillars
    for _ in range(thickness + 1):
        print((c * thickness).center(2 * thickness - 1) +
              (c * thickness).center(6 * thickness - 1))

    # Bottom Cone
    for i in range(thickness):
        print((c * (2 * (thickness - i) - 1)).center(2 * thickness - 1).rjust(6 * thickness))


if __name__ == "__main__":
    thickness = int(input().strip())
    print_h_pattern(thickness)
