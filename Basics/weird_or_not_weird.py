"""
Problem: Weird or Not Weird
Platform: HackerRank

Description:
Given an integer n, print:
- "Weird" if n is odd
- "Not Weird" if n is even and in range 2 to 5
- "Weird" if n is even and in range 6 to 20
- "Not Weird" if n is even and greater than 20

Approach:
- If number is odd → Weird
- If number is even:
    - Check if it lies between 6 and 20 → Weird
    - Otherwise → Not Weird

Optimized Logic:
- Combine conditions:
  (n is odd) OR (6 <= n <= 20) → Weird
  else → Not Weird

Time Complexity: O(1)
Space Complexity: O(1)
"""

def check_weird(n):
    if n % 2 != 0 or 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"


if __name__ == "__main__":
    n = int(input().strip())
    print(check_weird(n))
