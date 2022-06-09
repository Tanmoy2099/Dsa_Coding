w = 10
val = [20, 30, 10, 50]
wt = [1, 3, 4, 6]
n = len(wt)

mat = [[0 for i in range(w + 1)] for i in range(n + 1)]

for row in range(1, n + 1):
    for column in range(1, w + 1):
        valwithoutcurr = mat[row - 1][column]
        currweight = wt[row - 1]
        if currweight <= column:
            valwithcurr = val[row - 1]
            capacityremain = column - currweight
            valwithcurr += mat[row - 1][capacityremain]

        mat[row][column] = max(valwithcurr, valwithoutcurr)

print(f"Maximum profit is : {mat[n][w]}")
for i in range(len(mat)):
    print(mat[i])
