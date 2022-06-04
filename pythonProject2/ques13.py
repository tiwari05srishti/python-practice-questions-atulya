a = eval(input("enter the array"))
res = 0
for i in range(len(a)):
    res = res ^ a[i]
print(res)
