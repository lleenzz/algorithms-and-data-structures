def left(A, x):
    l = -1
    r = len(A)
    while r-l>1:
        m = (r+l)//2
        if A[m] >= x:
            r = m
        else:
            l = m
    return r

def right(A, x):
    l = -1
    r = len(A)
    while r-l>1:
        m = (r+l)//2
        if A[m] > x:
            r = m
        else:
            l = m
    return r

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
counts = []

A.sort()

for i in range(len(B)):
    counts.append( right(A, B[i]) - left(A, B[i]) )

print(*counts)