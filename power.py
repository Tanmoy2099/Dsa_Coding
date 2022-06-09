def pow(x,n):
    ans = 1
    for number in range(n):
        ans *=x
    return ans


print(pow(2,4))