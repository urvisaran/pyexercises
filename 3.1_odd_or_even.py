"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: number given as an input by the user
# 2. Process: using if else statements and a for loop to determine if the numbers from 1 to N are even or odd
# 3. Out: output is a list of numbers mentioned with even or odd mentioned in front of them
# 4. What happens on 0, on a negative number, on a very large number: on 0, it print 0 is neither even or odd, negative number prints "input is negative" and any number over 1000 prints that the number is too big for this exercise. 


# Your code below
n = int(input("enter a number:"))
if n == 0:
    print ("0 is not even or odd")
if n < 0:
    print ("number is negative")
if n > 1000:
    print ("number is too big for this exercise")
else:
    for i in range (1,n+1):
        if i%2 == 0:
            print (i, "is even")
        else:
            print (i, "is odd")