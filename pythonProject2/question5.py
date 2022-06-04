b=eval(input("enter array"))
#taking input of array b
a=[]

#assigning 0 to all values of a
for i in range(101):
    a.append(0)
#element of b is taken as index of a , for every element  in b , 1 is added to a's element
for i in b:
    a[i]+=1
#the index at which a has value 2 is the repeated one
for i in range(101):
    if(a[i]==2):
        print(i)

