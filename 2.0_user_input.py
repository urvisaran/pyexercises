"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: input given by the user, by using the input function. in my case, this was name and age 
# 2. Process: using the input entered by the user in a print statement
# 3. Out: the print statement using string concatenation 
# 4. My two fields, and what I would do with them: my two fields are name and age and i can use them to find the basic details of the user. 


# Your code below
question_1 = input("What is your name?")
question_2 = input ("What is your age?")
print ("My name is ", question_1, "and my age is ", question_2)

question_1 = input("What is your name?")
question_2 = int(input ("What is your age?"))
print ("My name is ", question_1, "and my age is ", question_2 + 1)

