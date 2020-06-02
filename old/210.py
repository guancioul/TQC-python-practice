"""
210 三角形判斷
請使用選擇敘述撰寫一程式，讓使用者輸入三個邊
長，檢查這三個邊長是否可以組成一個三角形。若
可以，則輸出該三角形之周長；否則顯示【Invalid
】。
 提示：檢查方法 = 任意兩個邊長之總和大於第三邊
長。
.index always returns the lowest index
list.remove 只能移除element
del list[index] 才能移除index
"""
triangle = []
num1 = int(input("enter first side:"))
num2 = int(input("enter second side:"))
num3 = int(input("enter third side:"))

triangle.append(num1)
triangle.append(num2)
triangle.append(num3)
tri_max = max(triangle)

del triangle[triangle.index(tri_max)]

if(tri_max < sum(triangle)):
	print(num1 + num2 + num3)
else:
	print("Invalid")