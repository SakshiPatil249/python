"""
Problem: Exceptions
Platform: HackerRank

Description:
Perform integer division for multiple test cases.

Handle:
1. ZeroDivisionError
2. ValueError

If an exception occurs,
print:
Error Code: <message>

Example Input:
3
1 0
2 $
3 1

Example Output:
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3

---------------------------------------------------
CONCEPT EXPLANATION
---------------------------------------------------

This problem introduces:
1. Exception handling
2. try-except blocks
3. Multiple exception handling

Exception handling is very important in:
- Real-world applications
- APIs
- Data processing
- User input validation

---------------------------------------------------
1) What is an Exception?
---------------------------------------------------

An exception is a runtime error
that interrupts normal execution.

Examples:
- Dividing by zero
- Invalid input conversion
- File not found


---------------------------------------------------
2) try-except Block
---------------------------------------------------

Syntax:

try:
    risky code

except:
    error handling code

Example:

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")


---------------------------------------------------
3) ZeroDivisionError
---------------------------------------------------

Occurs when dividing by zero.

Example:

10 // 0

Error:
ZeroDivisionError


---------------------------------------------------
4) ValueError
---------------------------------------------------

Occurs when invalid conversion happens.

Example:

int("$")

Error:
ValueError


---------------------------------------------------
5) Handling Multiple Exceptions
---------------------------------------------------

Syntax:

except (Error1, Error2) as e:

Example:

except (ValueError, ZeroDivisionError) as e:

Stores exception object in:
e


---------------------------------------------------
6) Exception Object
---------------------------------------------------

Example:

print(e)

Prints actual error message.

Example:
integer division or modulo by zero

"""


# ---------------------------------------------------
# Number of Test Cases
# ---------------------------------------------------
n = int(input())


# ---------------------------------------------------
# Process Each Test Case
# ---------------------------------------------------
for i in range(n):

    try:

        # Read two integers
        a, b = map(int, input().split())

        # Integer division
        print(a // b)

    # Handle both exceptions
    except (ValueError, ZeroDivisionError) as e:

        print("Error Code:", e)


# ---------------------------------------------------
# Alternative Approaches
# ---------------------------------------------------
"""
Alternative 1:
Separate exception blocks

try:
    a, b = map(int, input().split())
    print(a // b)

except ValueError as e:
    print("Error Code:", e)

except ZeroDivisionError as e:
    print("Error Code:", e)


---------------------------------------------------

Alternative 2:
Using generic Exception

except Exception as e:

Less recommended because:
- catches every error
- harder to debug
"""
