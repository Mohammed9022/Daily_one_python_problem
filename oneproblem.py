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


# Write a program to have a set with 18(int) and "18"(str) as a  value in it.

s = {18, "18", 18.1, (18, "18")} # Yes this will work because they all are different datatypes and sets are consume unique elements.

print(s)

# Create an empty dictionary and allow 4 friends to enter their favourite language as values and
# use keys as their names. Assume that teh names are unique

favDict = {}

a = input("Enter your programming language Afsar")
a = input("Enter your programming language Faisal")
a = input("Enter your programming language Sonal")
a = input("Enter your programming language Komal")

favDict["afsar"] = a
favDict["faisal"] = b
favDict["sonal"] = c
favDict["komal"] = d

print(favDict)


# Interview quetions (Interviewer will confusing you for asking this question)

# Can you change the values inside a list which is contained in set s.

#s = {8, 7, 12, "Afsar", [1, 2]}
#print(s) # This will throw an TypeError(unhashable type: 'list') 
# For this example we cannot change the list items in this set because sets are immutable.

## Write a program to find greatest of four numbers entered by the user.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if (num1 > num4):
	f1 = num1
else:
	f1 = num4

if (num2 > num3):
	f2 = num2
else:
	f2 = num3


if (f1 > f2):
	print(str(f1) + " is greatest")
else:
	print(str(f2) + " is greatest")



# Write a program to find out wheather a student is pass or fail. If it requires total 40% and
# at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.


sub1 = int(input("Enter first subject marks\n")) 
sub2 = int(input("Enter second subject marks\n")) 
sub3 = int(input("Enter third subject marks\n")) 

if (sub1 < 33 or sub2 < 33 or sub3 < 33):
	print("You are fail because you have less than 33% in one of the subjects")

elif (sub1 + sub2 + sub3 ) / 3 < 40:
	print("You are fail due to total percentage less than 40")
else:
	print("Congratualations! You have passed the exam")



# Write a program to detect these spam words. A spam comment is definded as a text containing following keywords:
#("make a lot of money", "buy now", "subscribe now", "click this")

text = input("Enter the text\n")

spam = False # If we have commented this line so we have to use else part of the ladder.

if ("make a lot of money" in text):
	spam = True

elif ("buy now" in text):
	spam = True

elif ("click this" in text):
	spam = True

elif ("subscribe this" in text):
	spam = True

# else:  # If we use spam=False in the top then we dont use these 2 lines.
# 	spam = False

if(spam):
	print("This text is spam")
else:
	print("This text is not spam")


# Write a program to find wheater a given username contains less thann 10 characters or not.

username = input("Enter username here: ")

length = len(username)

if (length < 10 ):
	print("Given characters are less than 10")

else:
	print("Given characters are greater than 10")



# Write a program to find given words are present in the list or not.

list_of_names = ["priyanka", "rizaa", "rakesh", "afsar", "faisal"]

name = input("Enter the name to check \n")

if (name in list_of_names):
	print("Your name is present in the list")
else:
	print("Your name is not present in the list")


# Write a program to print multiplication table of a given number using for loops and While loop

print("The Multiplication Table")
num = int(input("Enter number: "))


for i in range(1, 11):
	print(str(num) + " X " + str(i) + " = " + str(i*num))
#	print(f"{num}X{i}={i*num}") # We can also prints liks this type

# While loop

print("The Multiplication Table")
num = int(input("Enter Number: "))
n = 1

while num <= 10:
	print(f"{num} X {n} = {n*num}")
	n = n + 1


# Write a program to find wheater a given number is prime or not

num = int(input("Enter Numer: "))
prime = True

for i in range(2,num):
	if (num%i) == 0:
		prime = False
		break

if prime:
	print("This number is prime")
else:
	print("This number is not prime")


# Write a program to find the factorial number

num = int(input("Enter Number: "))
factorial = 1

for i in range(1, num+1):
	factorial = factorial * i
print(f"The factorial of {num} is {factorial}")


# Write a program to find the sum of numbers

num = int(input("Enter Number: "))
sum = 0

for i in range(0, num+1):
	sum = sum + i
print(f"The sum of {num} is {sum}")



# Write a program to find the sum of first n natural number using for loops

i = 1
sum = 0

num = int(input("Enter number: "))
while(i<num):
    sum += i
    i += 1
print(f"The sum of {num} natural number is {sum}")


# Write a program to print the star pattern 

n = int(input("Enter a number: "))

for i in range(1, n+1): # if we used only the output is came but the actual result will not come
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    for j in range(n-i):
        print(" ", end="")
    print("\n", end="")

# If we have created the multiplicaion table but we have to print the things in reversed form.

num = int(input("Enter Number: "))

for i in reversed(range(1, 11)):
	print(f"{num} X {i} = {i*num}")

# Write a program to to find the greatest of three numbers using the functions

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

def maximum(num1, num2, num3):
	if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    else:
        if (num2 > num3):
            return num2
        else:
            return num3

m = maximum(num1, num2, num3)
print("The value of the maximum is " + str(m))


# Write a program to convert the celcius to fehreheit.

def farh(cel):
	return (cel *(9/5)) + 32

c = 0
f = farh(c)
print("Fahreheit Temperature is " + str(f))


# How do we prevent the print() function to print a new line at the end.
# The default value of the print function at the end is \n that means new line at the every print statement.
print("Hello", end = " ")
print("How", end = " ")
print("Are", end = " ")
print("You ?", end = " ")


# Write a program to remove a given word from a string and strip at the same time

def remove_and_strip(string, word):
	newStr = string.replace(word, "")
	return newStr.strip()

new_word = "    Afsar is a boy      "
n = remove_and_strip(new_word, "Afsar")
print(n)


# Create a python function for Inches to centimeter converter


def cm_converter(inches):
    return (inches * 2.54)

a = int(input("Enter the inches value: "))
c = cm_converter(a)
print(f"The value of {a} Inches to Cm is {str(c)}")


# Create a python funcion to print the multiplication table of a given number 


def multiply(n):
    for i in range(1, 11):
	    print(str(n) + " X " + str(i) + " = " + str(i*n))

multiply(5)


# A file contains a list of word that contains["donkey", "mote", "kaddu"] multiple times. And we need to write a program which replace this word with ##### by updating 
#the same file. And we need this sample.txt file in our directory.

words = ["donkey", "mote", "kaddu"]

with open("sample.txt") as f:
    content = f.read()

for word in words:
	content = content.replace(word, "@@#$%^&^#@@")

with open("sample.txt", "w") as f:
    f.write(content)


# If we have a log file of any webapp and we need find out the word "python" in that log file so write a program to find that word.

content = True
i = 1

with open("sample.txt")as f:
        while content:
                content = f.readline()
                if "python" in content.lower():
                        print(content)
                        print(f"yes python is present in line number {i}")
                i += 1

# Write a program to make a copy of a text file example "thisfile.txt"

with open("thisfile.txt") as f:
	content = f.read()

with open("copyfile.txt", "w") as f:
	f.write(content)


# Write a progeram to find out wheater a file is identical and matches the content of another file.

file1 = "thisfile.txt"
file2 = "copyfile.txt"

with open(file1) as f:
	f1 = f.read()

with open(file2) as f:
	f2 = f.read()

if f1 == f2:
	print("Files are identical")
else:
	print("Files are not identical")


# Write a program to rename a file to "renamed_by_python.txt"

import os
oldname = "sample2.txt"
newname = "renamed_by_python.txt"

with open(oldname) as f:
        content = f.read()

with open(newname, "w") as f:
        f.write(content)

os.remove(oldname)


# Creating a calculator using conditional statement
print("Calculator")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))

print("Please select the operation 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")

a = int(input("Enter your choice: "))

if a == 1:
    result = num1 + num2 # For Addition
    print(result)
if a == 2:
    result = num1 - num2 # For Subtraction
    print(result)
if a == 3:
    result = num1 * num2 # For Multiplication
    print(result)
if a == 4:
    result = num1 / num2 # For Division
    print(result)