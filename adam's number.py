import math 

def numrev(x):
    y = 0
    counter = 0
    while x:
        z = x%10
        x = x//10
        y *= 10
        y += z
    return y

num = int(input("Enter your number:"))
copy = num**2
copy = numrev(copy)
copy = math.sqrt(copy)
copy = numrev(copy)
if num == copy:
    print(1)
else:
    print(0)
