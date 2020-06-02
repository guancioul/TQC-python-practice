"""
209 距離判斷
請使用選擇敘述撰寫一程式，讓使用者輸入一個點
的平面座標x和y值，判斷此點是否與點(5, 6)的距離
小於或等於15，如距離小於或等於15顯示【Inside】
，反之顯示【Outside】。
"""
import math

x = int(input("X:"))
y = int(input("Y:"))

dis = math.sqrt(math.pow(x-5,2) + math.pow(y-6,2))

if(dis <= 15):
	print("Inside")
else:
	print("Outside")