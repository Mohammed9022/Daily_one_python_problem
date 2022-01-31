# 1 write a python program to print the following string in a specific format.
"""Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are"""


#One way is this.
print("""
	Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are""") 

#another way is this.
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")



# 2 How do I write a python program to get the python verion.
import sys
print("Python version")
print(sys.version)


# 3 How to write a python code to get the current date and time.
"""Sample Output: 
Current date and time:
2014-07-05 14:34:14"""


import datetime
now = datetime.datetime.now()
print("Current date and time: ", now.strftime("%Y-%m-%d %H:%M:%S"))


#### Write a program which accepts the radious of a circle from the user and compute the area.

from math import pi

r = float(input("The radius of the circle is: "))
print("The area of circle with the radius: " + str(r) + " is: " + str(pi * r**2))


# Write a python program to find average of two numbers entered by the user.

a = input("Enter a first number: ")
b = input("Enter a second number: ")

a = int(a)
b = int(b)

avg = (a + b)/2
print("The average of a and b is", avg)


# Write a python program to calculate a square of a number entered by the user.

user = input("Enter the number: ")
user = int(user)
print("The square number is ", a**2)


# Write a program to create a template(like a job opportunity template on mail)

from datetime import date

letter = """
Dear <|NAME|>,
Greeting from ABC Co. Pvt. Ltd. \nI am happy to tell you about your job selection.
You are selected.
Have a nice day ahead!
Thanks and Regards,
Sim
Dated on <|DATE|>
"""

name = input("Enter Your Name\n")
dated = str(date.today())
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", dated)
print(letter)