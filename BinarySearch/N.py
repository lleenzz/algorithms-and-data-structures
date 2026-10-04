def good(A, K, B, M, X, m):
    d = (m - m//K)*A
    f = (m - m//M)*B
    return d + f >= X


A, K, B, M, X = map(int, input().split())

l = 0
r = 10**18 + 1
while r - l >1:
    m = (l + r) // 2
    if good(A, K, B, M, X, m):
        r = m
    else:
       l = m
print(r)

