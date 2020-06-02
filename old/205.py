"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個字
元，判斷它是包括大、小寫的英文字母（alphabet）
、數字（number）、或者其它字元（symbol）。例
如：a為英文字母、9為數字、$為其它字元。
"""
import re

s = input("please enter a char:")
if(re.match('[a-zA-Z]', s)):
    print(f"{s} is a alphabet")
elif(re.match('[0-9]', s)):
    print(f"{s} is a number")
else:
    print(f"{s} is a symbol")