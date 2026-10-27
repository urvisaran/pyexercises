"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: input is a dictionary of the five given items related to the brand 
# 2. Process: process includes reading the value assigned to a particular field, changing the value assigned to one field, deleting a field, showing the final list and then checking to see which error we get when a field that is not there in the dict is called (KeyError). 
# 3. Out: output is the final details of the campaign, after deleting a field and changing the value of one of the fields. 
# 4. My object, my five fields, and why those: my five fields are details from one of my favorite brands.


# Your code below
campaign = {
    "brand": "Miu Miu",
    "campaign_name": "Summer Collection 2027",
    "platform": "Instagram",
    "budget": 50000,
    "target_audience": "Women aged 18-30",
    "clicks": 12000
}
#reading a field
print ("brand:", campaign["brand"])
#changing a field
campaign["budget"] = 60000
print ("new budget:", campaign["budget"])
#removing a field
del campaign["clicks"]
#display every field with a value
print ("Final campaign details:")
for field, value in campaign.items():
    print(field, ":", value)



