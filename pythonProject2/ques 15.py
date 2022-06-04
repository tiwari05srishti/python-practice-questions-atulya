a = 'sriSHT##1625'
spcl = 0
num = 0
alph = 0

for i in range(0,len(a)):
    if ord(a[i]) in range(33 ,47,1):
        spcl+=1
    elif ord(a[i]) in range(48 ,57,1):
        num+=1
    elif ord(a[i]) in range(65, 90,1):
        alph+=1
    elif ord(a[i]) in range(97, 122,1):
        alph+=1

print("alphabets=",alph)
print("special characters =",spcl)
print("digits=", num)
