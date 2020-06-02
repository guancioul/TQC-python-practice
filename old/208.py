"""
208 十進位換算
請使用選擇敘述撰寫一程式，讓使用者輸入一個十
進位整數num(0 ≤ num ≤ 15)，將num轉換成十六進位
值。
 提示：轉換規則 = 十進位0~9的十六進位值為其本身
，十進位10~15的十六進位值為A~F。
"""
num = int(input("Please enter a number between 0~15:"))

if(num < 10):
	print(num)
elif(num == 10):
	print("A")
elif(num == 11):
	print("B")
elif(num == 12):
	print("C")
elif(num == 13):
	print("D")
elif(num == 14):
	print("E")
elif(num == 15):
	print("F")
else:
	print("Please enter a number between 0~15")