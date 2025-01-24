num = int(input("Enter ur numebr:"))

def factorial(x):
    if x == 0:
        return 1
    else:
        return x*factorial(x-1)

temp = 0
copy = str(num)
for i in copy:
    temp += factorial(int(i))

print(temp == num)

