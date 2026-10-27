"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: input is a list of items
# 2. Process: processing is done with basic printing as well as list functions such as sorting and couting the length of drinks
# 3. Out: output is the full list, one item of my choice from the list, the list in 
# 4. What my list is about, and what I computed from it: my list is a list of different alcohols and my computation is the sum of the length of the first three words


# Your code below
drinks = ["vodka","wine", "tequila", "beer", "gin", "whiskey", "rum", "rosé"]
print ("full list:", drinks)
print ("item of my choice:", drinks[3])
print ("sorted list:", sorted(drinks))
print ("total number of foods:", len(drinks))
# sum of length of first three items 
sum = len(drinks[0]) + len(drinks[1]) + len(drinks[2])
print ("sum of the length of the first three items:",  sum)