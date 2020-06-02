"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個正
整數，然後判斷它是否為偶數（even）。
"""

num = int(input("please enter a number:"))

if(num%2 == 0):
	print(f"{num} is a even number")
else:
	print(f"{num} is not a even number")