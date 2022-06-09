def jobScheduling(arr, k=3):
    ans = []
    length = len(arr)
    marked = [False for i in range(length)]
    for job in range(k, 0, -1):
        maxProfit = max(
            [
                arr[i][2]
                for i in range(length)
                if (arr[i][1] >= job and marked[i] == False)
            ]
        )
        for i in range(length):
            if arr[i][2] == maxProfit and marked[i] == False:
                ans.append(arr[i][0])
                marked[i] = True
                break
    return ans


arr = [
    ["a", 2, 100],  # Job Array
    ["b", 1, 19],
    ["c", 2, 27],
    ["d", 1, 25],
    ["g", 3, 30],
    ["e", 3, 15],
    ["f", 2, 100],
]

print(jobScheduling(arr, 3))
