from collections import deque

a = map(int, input().split())
b = map(int, input().split())

dq1 = deque(a)
dq2 = deque(b)

c = 0
while dq1 and dq2 and c <= 10**6:
    x1 = dq1.popleft()
    x2 = dq2.popleft()
    c += 1

    if x1 == 0 and x2 == 9:
        win = 1
    elif x1 == 9 and x2 == 0:
        win = 2
    elif x1 > x2:
        win = 1
    else:
        win = 2

    if win == 1:
        dq1.append(x1)
        dq1.append(x2)
    else:
        dq2.append(x1)
        dq2.append(x2)

if not dq2:
    print(f"first {c}")
elif not dq1:
    print(f"second {c}")
else:
    print("botva")
