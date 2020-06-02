"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個西
元年份，然後判斷它是否為閏年（leap year）或平年
。其判斷規則為：每四年一閏，每百年不閏，但每
四百年也一閏
"""
# 1992 is a leap year
# 1990 is not a leap year(every 100 years is not a leap year)
# 2000 is a leap year(every 400 years is a leap year)
year = int(input("Please enter a year:"))

if(year % 400 == 0):
    print(f"{year} is a leap year")
elif(year % 100 == 0):
    print(f"{year} is not a leap year")
elif(year % 4 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")