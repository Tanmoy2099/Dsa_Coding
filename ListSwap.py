import random


def listSwap(lst, pos1, pos2):

    lst[pos1 - 1], lst[pos2 - 1] = lst[pos2 - 1], lst[pos1 - 1]
    return lst


# L = [1, 2, 3,4,5,6,7,8,65,43,56,23,34,35,56]
L = []
for item in range(10):
    i = (int)(random.random() * 100)
    L.append(i)

print(L)
a = int(input())
b = int(input())
print(listSwap(L, a, b))
