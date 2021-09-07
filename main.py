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


