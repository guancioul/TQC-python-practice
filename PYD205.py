# TODO
import re

s = input()

if(re.match("[a-zA-Z]", s)):
	print(f"{s} is an alphabet.")
elif(re.match("[0-9]", s)):
	print(f"{s} is a number.")
else:
	print(f"{s} is a symbol.")