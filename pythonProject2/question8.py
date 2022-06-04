ints=[]
sample = input("enter sample")
for i in range(len(sample)):
    if ord(sample[i]) in range(49,57):
        ints.append(sample[i])

sum = 0

for i in range(len(ints)):
    sum+=int(ints[i])

print(sum)


