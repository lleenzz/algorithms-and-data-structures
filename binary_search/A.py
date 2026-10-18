def binary_search(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l+r)//2

        if arr[m] < x:
            l = m
        else:
            r = m
    if r < len(arr) and arr[r] == x:
        return True
    return False


n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


for el in b:
    if binary_search(a, el):
        print("YES")
    else:
        print("NO")

