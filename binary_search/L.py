def good(N, R, C, m):
    count = 0
    i = 0
    while i <= N - C:
        n = h[i + C - 1] - h[i]
        if n <= m:
            count += 1
            i+=C
        else:
            i += 1
    return count >= R


N, R, C = map(int, input().split())

h = []
for _ in range(N):
    h.append(int(input()))

h.sort()

l = -1
r = 10**9
while r - l >1:
    m = (l + r) // 2
    if good(N, R, C, m):
        r = m
    else:
       l = m
print(r)

