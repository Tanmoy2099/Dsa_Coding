lst = [45, 47, 48, 96, 58, 87, 5]

start = 0
new_lst = sorted(lst)
end = int(len(lst) - 1)

print(new_lst[::-1])
print(list(reversed(new_lst)))

while start <= end:
    lst[start], lst[end] = lst[end], lst[start]
    start += 1
    end -= 1
print(lst)
