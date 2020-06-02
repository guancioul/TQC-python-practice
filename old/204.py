"""
請使用選擇敘述撰寫一程式，讓使用者輸入兩個整
數a、b，然後再輸入一算術運算子 (+、-、*、/、//
、%） ，輸出經過運算後的結果。
"""
num1 = int(input("input num1:"))
num2 = int(input("input num2:"))
operator = input("input a operator:")

if(operator == "+"):
    print(num1 + num2)
elif(operator == "-"):
    print(num1 - num2)
elif(operator == "*"):
    print(num1 * num2)
elif(operator == "/"):
    print(num1 / num2)
elif(operator == "//"):
    print(num1 // num2)
elif(operator == "%"):
    print(num1 % num2)
else:
    print("cannot find the operator")