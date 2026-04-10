"""
Problem: Shoe Shop Earnings
Platform: HackerRank

Description:
A shop owner has a collection of shoes of different sizes.
Customers request a shoe size and offer a price.

If the requested size is available, the shop sells the shoe and earns the money.
Each shoe can only be sold once.

Input:
10
2 3 4 5 6 8 7 6 5 2
6
6 55
6 45
6 55
4 40
18 60
10 50

Output:
200

Approach:
- Use Counter to track available shoe sizes
- For each customer:
    - Check if requested size exists
    - If yes, sell it and update inventory

"""

from collections import Counter

def calculate_earnings():
    # Read number of shoes
    num_shoes = int(input())

    # Count frequency of each shoe size
    sizes = Counter(map(int, input().split()))

    # Number of customers
    num_customers = int(input())

    total_earned = 0  # total money earned

    for i in range(num_customers):
        size, price = map(int, input().split())

        # Sell only if size is available
        if sizes[size] > 0:
            total_earned += price
            sizes[size] -= 1

    print(total_earned)


if __name__ == "__main__":
    calculate_earnings()
