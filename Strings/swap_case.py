"""
Problem:Swap Case
Platform:HackerRank

Description:
Given a string, convert all lowercase letters to uppercase
and all uppercase letters to lowercase.

Input:
Www.HackerRank.com

Output:
wWW.hACKERrANK.COM

Approach:
1. Built-in method using swapcase()
2. Manual approach using loop and conditions
3. Pythonic approach using list comprehension

"""

 """
    Approach 1: Using built-in function
 """
def swap_case_builtin(s):
   
    return s.swapcase()



  """
    Approach 2: Manual character-by-character conversion
  """
def swap_case_manual(s):
  
    result = ""

    for ch in s:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            result += ch

    return result



    """
    Approach 3: Using list comprehension (Pythonic way)
    """

def swap_case_pythonic(s):

    return ''.join(
        ch.lower() if ch.isupper() else ch.upper()
        for ch in s
    )


if __name__ == "__main__":
    s = input().strip()

    # Default 
    print(swap_case_builtin(s))

    # Uncomment below to test other methods
    # print(swap_case_manual(s))
    # print(swap_case_pythonic(s))
