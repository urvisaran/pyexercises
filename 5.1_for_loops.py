"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: input is the list of drinks
# 2. Process: it starts with the first position and then uses a for loop for every item in the list to show its position and length
# 3. Out: number of letters in each drink along with its' position
# 4. What I compute for each item, and why it is worth showing: it shows the position of each drink along with the number of letters in each drink


# Your code below
drinks = ["vodka","wine", "tequila", "beer", "gin", "whiskey", "rum", "rosé"]
position = 1

for drink in drinks:
    print(drink, "- Position:", position, "- Number of letters:", len(drink))
    position = position + 1
