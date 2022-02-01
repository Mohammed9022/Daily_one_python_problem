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

# Write a program to enter seven fruits names in a list entered by the user.

f1 = input("Enter Fruit Number 1: ")
f2 = input("Enter Fruit Number 2: ")
f3 = input("Enter Fruit Number 3: ")
f4 = input("Enter Fruit Number 4: ")
f5 = input("Enter Fruit Number 5: ")
f6 = input("Enter Fruit Number 6: ")
f7 = input("Enter Fruit Number 7: ")

myList = [f1, f2, f3, f4, f5, f6, f7]
print(myList)

# Write a program to accept the 6 students marks in the sorted manner

m1 = int(input("Enter Marks For Student 1: "))
m2 = int(input("Enter Marks For Student 2: "))
m3 = int(input("Enter Marks For Student 3: "))
m4 = int(input("Enter Marks For Student 4: "))
m5 = int(input("Enter Marks For Student 5: "))
m6 = int(input("Enter Marks For Student 6: "))

myMarksList = [m1, m2, m3, m4, m5, m6]
myMarksList.sort()
print(myMarksList)

# Write a program to sum a list of 4 numbers


list1 = [23, 5, 45, 6]
print(list1[0] + list1[1] + list1[2] + list1[3]) # One way is this

# And the another way is this

list1 = [23, 5, 45, 6]
print(sum(list1))

# Write a program to count a zeros in the given tuple (a = (3,2,0,1,0,0,5))

a = (3,2,0,1,0,0,5)
print(a.count(0))


# Write a program to Create the Dictionary of english to hindi translation.

myDict = {
	"Bad" : "Kharab",
	"Tolerate" : "Sahna",
	"good" : "accha",
	"Describe" : "Darshana"
}

print("The options are", list(myDict.keys()))

a = input("Enter the word\n")
print("The meaning of your word is: ", myDict.get(a)) # the get function will not return an error 
# It returns the None value (if the contents are not present in the dictionary)


# write a program to input 8 numbers from the user and display them in unique numbers (using sets)

num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))
num3 = int(input("Enter number 3\n"))
num4 = int(input("Enter number 4\n"))
num5 = int(input("Enter number 5\n"))
num6 = int(input("Enter number 6\n"))
num7 = int(input("Enter number 7\n"))
num8 = int(input("Enter number 8\n"))

s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)
