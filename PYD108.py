import math
# TODO
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())

print("(", x1, ",", y1, ")")
print("(", x2, ",", y2, ")")
d = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))

print("Distance = %.4f" % d)