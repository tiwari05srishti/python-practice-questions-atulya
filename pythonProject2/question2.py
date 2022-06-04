x = int(input("number: "))
y = [int(x) for x in str(x)]
z = []
a = y[-1]
b = y[-2]
c = y[-3]
d = y[-4]
z.append(d)
z.append(c)
z.append(b)
z.append(a)

print(z);
