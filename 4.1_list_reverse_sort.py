"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: input is the same list as last time
# 2. Process: changing the order of the list on the basis of the alphabets and lengths, etc.
# 3. Out: output was the different types of orders of the list
# 4. My four orders, and which ones modify the original: alphabetical order, reverse of the alphabetical order, reverse overall order of the list and order of the list by word length. all of these modify the original


# Your code below
drinks = ["vodka","wine", "tequila", "beer", "gin", "whiskey", "rum", "rosé"]
print ("original list:", drinks)
print ("alphabetical order:", sorted(drinks))
print ("reversed alphabetical order:", sorted(drinks, reverse=True))
print ("reverse order of the list:", list(reversed(drinks)))
print ("order by word length:", sorted(drinks, key=len))
print ("original list again:", drinks)
