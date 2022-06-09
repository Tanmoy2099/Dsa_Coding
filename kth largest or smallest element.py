'''
Functions which return kth largest or smallest element in an array
author : Tanmoy Nath

'''
def kth_smallest(data, k): #call for kth smallest element
    lo = 0
    hi = len(data) - 1
    index = lo + k - 1
    return kth_num(data, lo, hi, index)


def kth_largest(data, k):#call for kth largest element
    lo = 0
    hi = len(data) - 1
    index = hi - k + 1
    # print(data[index])
    return kth_num(data, lo, hi, index)


def kth_num(data, lo, hi, index): #dividing the array to the relavent range
    kth = qS(data, lo, hi)
    # print(data[lo:hi], kth)
    if kth < index:
        return kth_num(data, kth +1, hi, index)
    elif kth > index:
        return kth_num(data, lo, kth, index)

    return data[kth]


def qS(data, lo, hi): # swaping till the right element placed in the right index
    pivot = lo
    j = hi
    i = lo
    while i < j:
        while data[i] <= data[pivot] and i < j:
            i += 1
        while data[j] >= data[pivot] and pivot < j:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
    if(j>pivot):
        data[pivot], data[j] = data[j], data[pivot]
    # print(data[lo:hi])
    return j


data = [58, 36, 75, 21, 42, 15, 78, 152, 5, 9, 111, 22, 99, 44]
# data = [-1,-1]

print(kth_largest(data, 2))
# print(kth_smallest(data, 4))
print(sorted(data))
