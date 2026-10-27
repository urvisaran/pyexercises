"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: an inputted sentence by the user
# 2. Process: using string functions for string transformations on the input
# 3. Out: the string transformations
# 4. My four transformations, and when each is useful: upper can be used to make all the letters capital, lower makes all the letters lowercase, reverse can reverse everythin in the sentence and strip will remove any leading and trailing whitespaces.


# Your code below
sentence = input("Enter a sentence:")
print ("Uppercase:", sentence.upper())
print ("Lowercase:", sentence.lower())
print ("Stripped:", sentence.strip())
print ("Reverse:", sentence[::-1])
