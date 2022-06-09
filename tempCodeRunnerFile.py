    max_num = max(arr)
    count = 0
    for i in arr:
        if arr[i] == max_num:
            count += 1
        if count > 1:
            return 0
    return 1