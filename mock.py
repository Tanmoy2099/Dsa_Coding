def police(data, k):
    result = police = thief = x = y = 0

    if data[i]=="P" and abs(x-y)<=k:
        if thief>0:
            police+=1
            x+=1
            y+=1
            result+=1
        else:
            thief+=1
            y+=1
    police+=1

    return result


data = ["P", "T", "T", "P", "T"]


print(police(data, 1))

2 4 8 9 7 17  4
8 9 9 7 8 4 2
