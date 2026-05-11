"""
Problem: Merge the Tools
Platform: HackerRank

Description:
Split the string into substrings of size k.
For each substring:
- Remove duplicate characters
- Preserve original order

Print each processed substring on a new line.

Example:
Input:
AABCAAADA
3

Substrings:
AAB
CAA
ADA

After removing duplicates:
AB
CA
AD

Output:
AB
CA
AD

---------------------------------------------------
CONCEPT EXPLANATION
---------------------------------------------------

This problem focuses on:
1. String slicing
2. Removing duplicates
3. Maintaining character order
4. Loop traversal

---------------------------------------------------
1) String Slicing
---------------------------------------------------

Syntax:

string[start:end]

Example:

s = "ABCDEFG"

s[0:3]

Output:
ABC

In this problem:

string[i:i+k]

Extracts substrings of size k.


---------------------------------------------------
2) Splitting into Equal Parts
---------------------------------------------------

Loop:

for i in range(0, len(string), k)

Example:
String length = 9
k = 3

Indices:
0, 3, 6

Substrings:
0-2
3-5
6-8


---------------------------------------------------
3) Removing Duplicates While Preserving Order
---------------------------------------------------

Important:
We cannot use set() directly because:
- sets do NOT preserve order

Example:

"AAB"

Using set():
{'A', 'B'}

Order may change.

Instead:

if ch not in result:

This keeps:
- first occurrence
- original order


---------------------------------------------------
4) Example Walkthroug
---------------------------------------------------

Substring:
"AAB"

Step 1:
'A' not in result
result = "A"

Step 2:
'A' already exists
skip

Step 3:
'B' not in result
result = "AB"

Final:
"AB"

"""


# ---------------------------------------------------
# Function Definition
# ---------------------------------------------------
def merge_the_tools(string, k):

    # Traverse string in chunks of size k
    for i in range(0, len(string), k):

        # Extract substring
        substring = string[i:i+k]

        # Store unique characters
        result = ""

        # Traverse each character
        for ch in substring:

            # Add only if not already present
            if ch not in result:
                result = result + ch

        # Print processed substring
        print(result)


# ---------------------------------------------------
# Main Execution
# ---------------------------------------------------
if __name__ == '__main__':

    string, k = input(), int(input())

    merge_the_tools(string, k)


# ---------------------------------------------------
# Alternative Approaches
# ---------------------------------------------------
"""
Alternative 1:
Using list for tracking

def merge_the_tools(string, k):

    for i in range(0, len(string), k):

        substring = string[i:i+k]

        seen = []

        for ch in substring:
            if ch not in seen:
                seen.append(ch)

        print("".join(seen))


---------------------------------------------------

Alternative 2:
Using dict.fromkeys()

def merge_the_tools(string, k):

    for i in range(0, len(string), k):

        substring = string[i:i+k]

        print("".join(dict.fromkeys(substring)))

Reason:
Python dictionaries preserve insertion order.
"""
