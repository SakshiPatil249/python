"""
Problem: String Formatting (Number Systems)
Platform: HackerRank

Description:
Given an integer n, print numbers from 1 to n in:
- Decimal
- Octal
- Hexadecimal (uppercase)
- Binary

Each value should be right-aligned and padded to match
the width of the binary representation of n.

Input:
17

Output:
(Formatted columns as shown)

Approach:
- Compute width using binary representation of n
- For each number:
    - Convert to different bases
    - Remove prefixes (0o, 0x, 0b)
    - Align using rjust()

"""


def print_formatted(number):
    # Width based on binary representation
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]              # remove '0o'
        hexa = hex(i)[2:].upper()       # remove '0x' and uppercase
        binary = bin(i)[2:]             # remove '0b'

        print(
            decimal.rjust(width),
            octal.rjust(width),
            hexa.rjust(width),
            binary.rjust(width)
        )


if __name__ == "__main__":
    n = int(input().strip())
    print_formatted(n)
