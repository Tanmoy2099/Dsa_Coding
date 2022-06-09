import heapq as h
def thirdLargest(nums):
    if len(set(nums))<3:
        return max(nums)
    return sorted(list(set(nums)))[-3]



data = [9, 8, 8,8,8,8,7,7,7,7,7, 2]
print(thirdLargest(data))
data.sort(reverse=True)
h.heapify(data)
print(data)