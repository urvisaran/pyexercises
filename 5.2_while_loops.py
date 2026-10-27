"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: input is the minimum and maximum number of attempts, along with the creation of the variable answer with an empty string to use in the while loop
# 2. Process: the while loop decides that when the conditions are met, the answer will be printed accordingly and the loop stops accordingly, using break
# 3. Out: prints the total number of attempts along with the list of attempts
# 4. My stop condition, my attempt limit, my summary: stop condition, is if the user says no to conintuing or if the max number of attempts is reached


# Your code below

attempts = 0
max_attempts = 5

answer = ""

while answer != "no" and attempts < max_attempts:
    answer = input("Do you want to continue? ").strip().lower()
    attempts = attempts + 1

    if answer == "yes":
        print("continue")
    if attempts == max_attempts:
        print ("max number of attempts reached")
        break
    if answer == "no":
        print("stopping.")
        break
    else:
        print("enter yes or no")

print("total attempts:", attempts)

    
