"""
Problem: Mutate String
Platform: HackerRank

Description:
Given a string, replace the character at a specific index
with a new character.

Since strings are immutable in Python, we create a new string.

Input:
abracadabra
5 k

Output:
abrackdabra

Approach:
1. Use string slicing:
   - Take part before index
   - Add new character
   - Add remaining part after index


"""


def mutate_string(s, position, character):
    """
    Approach 1: Using slicing (recommended)
    """
    return s[:position] + character + s[position + 1:]


def mutate_string_ls(s, position, character):
    """
    Approach 2: Convert to list and modify
    """
    s_list = list(s)
    s_list[position] = character
    return ''.join(s_list)


if __name__ == "__main__":
    s = input().strip()
    i, c = input().split()

    # Recommended method
    print(mutate_string(s, int(i), c))

    # Uncomment to test alternative
    # print(mutate_string_ls(s, int(i), c))
