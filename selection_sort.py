def selection(data):
    minv = 0
    for i in range(len(data)):
        minv = i
        for j in range(i + 1, len(data)):
            if data[minv] > data[j]:
                minv = j

        data[minv], data[i] = data[i], data[minv]
    return data


ans = [10, 5, 1, 13, 8, 4, 7]
print(ans)
print(selection(ans))
