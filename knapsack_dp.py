w = 10
val = [20, 30, 10, 50]
wt = [1, 3, 4, 6]
n = len(wt)

mat = [[0 for i in range(w + 1)] for i in range(n + 1)]

for item in range(1, n + 1):
    for capacity in range(1, w + 1):
        maxValWithoutCurr = mat[item - 1][capacity]
        weightOfCurr = wt[item - 1]

        if capacity >= weightOfCurr:
            maxValWithCurr = val[item - 1]

            remainingCapacity = capacity - weightOfCurr
            maxValWithCurr += mat[item - 1][remainingCapacity]

        mat[item][capacity] = max(maxValWithoutCurr, maxValWithCurr)

print(f"Maximum profit is : {mat[n][w]}")
for i in range(len(mat)):
    print(mat[i])
