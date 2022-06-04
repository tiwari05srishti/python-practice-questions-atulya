lower = int(input("enter the lower value:"))
upper = int(input("enter the upper value:"))

for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                print(num)