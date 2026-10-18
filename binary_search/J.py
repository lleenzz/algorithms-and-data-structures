def good(a, b, m, w, h, n):
    if w//(a+2*m)* (h// (b+2*m)) >=n or h //(a+2*m)* (w // (b+2*m)) >=n:
        return True
    return False


n, a, b, w, h = map(int, input().split())

l = 0
r = max(w, h) + 1
while r - l >1:
    m = (l + r) // 2
    if good(a, b, m, w, h, n):
        l = m
    else:
        r = m
print(l)

