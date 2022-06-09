import heapq


def mincost(a, m):
    heapq.heapify(a)
    if len(a) <= 1:
        return m
    n = heapq.heappop(a) + heapq.heappop(a)
    heapq.heappush(a, n)
    m += n
    return mincost(a, m)

m = 0
a = [2, 5, 4, 8, 6, 9, 1]
print(mincost(a, m))