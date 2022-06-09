# Input: arr[] = {2, 4, 8, 2}, K = 4
# Output: 2
# Explanation:
# Following sequence of operations are required to be performed:
# Operation 1: Splitting arr[1] (= 4) to {2, 2} modifies the array to {2, 2, 2, 8, 2}.
# Operation 2: Splitting arr[3] (= 8) to {2, 6} modifies the array to {2, 2, 2, 2, 6, 2}.
# Operation 3: Splitting arr[4] (= 6) to {2, 4} modifies the array to {2, 2, 2, 2, 2, 4, 2}.
# Operation 4: Splitting arr[5] (= 4) to {2, 2} modifies the array to {2, 2, 2, 2, 2, 2, 2, 2}.
# After completing the above operations, the maximum element present in the array is 2.

# Input: arr[] = {7, 17}, K = 2
# Output: 7

# Python3 program for the above approach

# Function to check if all array
# elements can be reduced to at
# most mid by at most K splits


def possible(A, N, mid, K):
    count = 0
    for i in range(N):
        count += (A[i] - 1) // mid
    return count <= K


def minimumMaximum(A, N, K):
    lo = 1
    hi = max(A)
    while lo < hi:
        mid = (lo + hi) // 2
        if possible(A, N, mid, K):
            hi = mid
        else:
            lo = mid + 1
    return hi


if __name__ == "__main__":
    # arr = [2, 4, 8, 2]
    arr = [7, 17]
    K = 2
    N = len(arr)
    print(minimumMaximum(arr, N, K))
