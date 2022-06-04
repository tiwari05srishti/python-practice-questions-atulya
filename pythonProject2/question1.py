
def arrange(a,b):
    if b=="asc":
        a.sort()
    elif b=="dsc":
        a.sort(reverse=True)
    return a
#checking
a=[1,9,5,6,2,3]
b="none"
print(arrange(a,b))