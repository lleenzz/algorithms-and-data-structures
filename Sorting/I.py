a = list(input())
b = list(input())

n = len(a)
c = 0
for i in range(n):
    if a[i] in b:
        c += 1
        b.remove(a[i])
if c == n:
    print("YES")
else:
    print("NO")

