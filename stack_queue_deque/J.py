N = int(input())
for _ in range(N):
    data = list(map(float, input().split()))
    n = data[0]
    a = data[1:]

    stack = []
    need_b = sorted(a)
    ind = 0

    for el in a:
        stack.append(el)
        while stack and stack[-1] == need_b[ind]:
            stack.pop()
            ind += 1

    if not stack:
        print(1)
    else:
        print(0)

