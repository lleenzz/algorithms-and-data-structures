def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while r - l > 1:
        m = (l+r)//2
        if arr[m] < x:
            l = m
        else:
            r = m



    if abs(arr[l]-x) <= abs(arr[r]-x):
        return arr[l]
    else:
        return arr[r]



n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


for el in b:
    print(binary_search(a, el))
