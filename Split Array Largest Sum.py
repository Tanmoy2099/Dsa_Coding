def minMaxSum(data, m): # using binary search tree
    hi = sum(data)
    lo = max(data)
    while lo < hi:
        mid = (lo + hi) // 2
        if isMax(data, mid, m):
            hi = mid
        else:
            lo = mid + 1
    return hi


def isMax(data, mid, m):
    count = 1
    sum = 0
    for num in data:
        sum += num
        if sum > mid:
            count += 1
    return count <= m


# data = [7, 2, 5, 10, 8]

data = [1,4,4]

print(minMaxSum(data, 3))
