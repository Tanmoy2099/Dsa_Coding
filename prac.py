def mincost(a, m):
    a.sort()
    if len(a) <= 1:
        return m
    n = a.pop(0) + a.pop(0)
    a.append(n)
    m += n
    return mincost(a, m)


m = 0
a = [2, 5, 4, 8, 6, 9]
print(mincost(a, m))
