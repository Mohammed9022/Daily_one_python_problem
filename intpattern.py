#print the pattern of 123...n

def int_number(n):
	num = 1
	for i in range(0, n):
		num = 1	
		for j in range(0, i+1):
			print(num, end = " ")
			num = num + 1
		print("\r")

num = 5
int_number(num)



# print the this pattern also

rows = 5
for i in range(0, rows):
	for j in range(0, i+1):
		print("*", end = " ")
	print("\r")


# And shorthand code 

rows = 5
for i in range(1, rows+1):
	print("*" *i)