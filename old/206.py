"""
206 等級判斷
請使用選擇敘述撰寫一程式，根據使用者輸入的分
數顯示對應的等級。標準如下表所示：
 分 數 等 級
80 ~ 100 A
70 ~ 79 B
60 ~ 69 C
<= 59 F
"""
score = int(input("Please enter a score:"))

if(score >= 80 and score <= 100):
	print("A")
elif(score >= 70 and score <= 79):
	print("B")
elif(score >= 60 and score <= 69):
	print("C")
elif(score >= 0 and score <= 59):
	print("F")
else:
	print("Please enter a score between 100~0")