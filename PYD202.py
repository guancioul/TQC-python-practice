# TODO
num = int(input())

if(num%5 == 0 and num % 3 == 0):
	print("%d is a multiple of 3 and 5." % num)
elif(num % 3 == 0):
	print("%d is a multiple of 3." % num)
elif(num % 5 == 0):
	print("%d is a multiple of 5." % num)
else:
	print("%d is not a multiple of 3 or 5." % num)
"""
_ is a multiple of 3 and 5.
_ is a multiple of 3.
_ is a multiple of 5.
_ is not a multiple of 3 or 5.
"""