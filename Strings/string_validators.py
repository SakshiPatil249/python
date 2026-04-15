"""
Problem: String Validators
Platform: HackerRank

Description:
Given a string, check if it contains:
- Any alphanumeric characters
- Any alphabetical characters
- Any digits
- Any lowercase characters
- Any uppercase characters

Print True or False for each condition on separate lines.

Input:
qA2

Output:
True
True
True
True
True

Approach:
- Iterate through each character in the string.
- built-in string methods:
    - isalnum()
    - isalpha()
    - isdigit()
    - islower()
    - isupper()
- any() : to check if at least one character satisfies the condition


"""


def string_validators(s):
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


if __name__ == "__main__":
    s = input().strip()
    string_validators(s)
