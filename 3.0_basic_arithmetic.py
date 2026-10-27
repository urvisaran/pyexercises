"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the number input by the user (in an int format)
# 2. Process: the four arithmetic operations performed using the four operators within the print statement along with an if and else statement for the division (since 0 cannot be a denominator)
# 3. Out: the answers of the operations
# 4. What happens when the second number is zero, and why: when the second number is zero, without the if and else operator, the code will throw a ValueError 


# Your code below
number1 = float(int(input("enter the first number:")))
number2 = float(int(input("enter the second number:")))
#operations:
print ("addition:", number1+number2)
print ("subtraction:" , number1 - number2)
print ("multiplication:", number1*number2)

if number2 == 0:
    print ("this division cannot be performed")
else:
    print ("division:", number1/number2)

