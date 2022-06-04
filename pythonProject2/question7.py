def max_freq(arr = [1,5,5,6,5,8,9,0,3]):
    print ("Original list : " + str(arr))
    res = max(set(arr), key = arr.count)
    print ("Most frequent number is : " + str(res))

max_freq()